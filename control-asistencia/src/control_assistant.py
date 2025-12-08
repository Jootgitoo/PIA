import datetime
import webbrowser
import json
import os
import pyttsx3
import speech_recognition as sr
import cv2
import json
import face_recognition
from pathlib import Path
import face_recognition as fr
import time
    
def saludo():
    """
    El sistema te saluda según la hora del día.
    """
    
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        momento = 'Buenas noches.'
    elif 6 <= hour.hour < 13:
        momento = 'Buenos días.'
    else:
        momento = 'Buenas tardes.'
    talk(f'{momento}. Por favor, pon la cara enfrente de la cámara para comprobar tu identidad.')
    capturar_foto_inicial()
    



def capturar_foto_inicial():
    """
    Abre la cámara, muestra una ventana durante 2 segundos y toma la foto automáticamente.
    """
    
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return None

    # Guardamos el tiempo en el que empieza el proceso
    tiempo_inicio = time.time()
    
    frame = None
    ret = False

    # Mantenemos el bucle abierto solo mientras hayan pasado menos de 2 segundos
    while (time.time() - tiempo_inicio) < 5:
        ret, frame = cam.read()
        
        if not ret:
            print("Error: No se pudo leer la imagen de la cámara.")
            break

        # Mostramos la ventana con lo que ve la cámara
        cv2.imshow("Ajustate - La foto se tomara en 2 segundos", frame)
        
        # Necesario para que la ventana de OpenCV se refresque y muestre la imagen
        cv2.waitKey(1)

    # Una vez pasados los 5 segundos, cerramos cámara y ventana
    cam.release()
    cv2.destroyAllWindows()

    if not ret or frame is None:
        print("Error: No se pudo capturar la imagen final.")
        return None

    actual_user_image = "fotos/usuario_actual.jpg"
    
    # Guardamos la imagen (el último frame capturado antes de cerrar)
    cv2.imwrite(actual_user_image, frame)

    talk(f"Foto inicial capturada")
    comprobar_identidad(actual_user_image, "bbdd/usuarios.json")


def comprobar_identidad(imagen_usuario, json_usuarios):

    # Carga el Json con usuarios
    with open(json_usuarios, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("Datos de usuarios cargados correctamente.")

    # Rutas de las imagenes que se van a utilizar (la primera es la del usuario a identificar y el resto las de la base de datos)
    lista_rutas = [imagen_usuario]
    print("Ruta de la imagen del usuario a identificar añadida.")

    usuarios = data["usuarios"]
    # Añadir todas las fotos registradas
    for user in usuarios:
        lista_rutas.append(user["foto"])
    print("Rutas de las imágenes de la base de datos añadidas.")

    # 2. Cargar imágenes con TUS MÉTODOS
    fotos = cargar_imagenes(lista_rutas)
    print("Imágenes cargadas correctamente.")
    fotos = asignar_perfil_color(fotos)
    print("Perfil de color asignado correctamente.")

    try:
        codificaciones = get_cod_faces(fotos)
    except Exception as e:
        print("Error al obtener codificaciones de las caras:", e)
        talk("No se ha detectado una cara válida en alguna de las imágenes. Por favor, inténtalo de nuevo.")
        return  # Salir de la comprobación para evitar seguir con codificaciones inválidas
    print("Codificaciones obtenidas correctamente.")

    # Comparar foto de control (primer índice) contra las demás
    resultados = compare_all_with_control(codificaciones)
    print("Comparación control --> usuarios realizada correctamente.")

    # Interpretar resultados
    usuario_encontrado = False
    
    for i in range(1, len(resultados)):
        if resultados[i]['misma_cara'][0]:
            nombre = usuarios[i-1]['nombre']
            talk(f"Usuario reconocido: Bienvenido {nombre}")
            request()
            
            usuario_encontrado = True
            break
    
    if not usuario_encontrado:
        talk("El usuario no ha sido reconocido. ¿Desea registrarse?")
        request_usr = audio_to_text().lower()
        
        while not "si" in request_usr:
            talk("No te he entendido. ¿Deseas registrarte? Por favor, responde sí o no.")
            request_usr = audio_to_text().lower()
        
        if "si" in request_usr:
            registrar_usuario()
        

            
def cargar_imagenes(path_list):
    """
    Lista de rutas de imágenes a cargar.
    Las reconoce y carga
    
    :param path_list: Descripción
    """
    # La primera será una foto de control, el resto de pruebas
    fotos = []
    for path in path_list:
        fotos.append(fr.load_image_file(path))
    return fotos           

def asignar_perfil_color(fotos_list):
    """
    Asigna el perfil de color RGB a las imágenes cargadas.
    
    :param fotos_list: Descripción
    """
    for i in range(len(fotos_list)):
        fotos_list[i] = cv2.cvtColor(fotos_list[i], cv2.COLOR_BGR2RGB)
    return fotos_list 

# top, right, botton, left
def localizar_cara(fotos_list):
    locations = []
    for i in fotos_list:
        locations.append(fr.face_locations(i)[0]) #puede detectar más caras... nos quedamos con la primera
    return locations


def get_cod_faces(fotos_list):
    cod_faces = []
    for idx, img in enumerate(fotos_list):
        enc = fr.face_encodings(img)
        if not enc:
            raise ValueError(f"No se detectó ninguna cara en la imagen índice {idx}")
        cod_faces.append(enc[0])
    return cod_faces


def compare_all_with_control(cara_cod_list):
    results = []
    for i,fc in enumerate(cara_cod_list):
        if i > 0:
            # Con fr.compare_faces([control_cod], cara_cod_comparar, 0.3) podemos modificar el límite por el que determinaría si es true
            diferencias = {'misma_cara': fr.compare_faces([cara_cod_list[0]], fc),
                           'distancia': fr.face_distance([cara_cod_list[0]], fc)}
        elif i == 0:
            diferencias = { 'misma_cara': 'control',
                            'distancia': '0'}
        results.append(diferencias)

    return results

def registrar_usuario():
    talk('Dime el nombre del usuario')
    user_name = audio_to_text().lower()
    talk('Nombre guardado correctamente')
    
    talk('Dime el dni del usuario')
    user_dni = audio_to_text().lower()
    talk('DNI guardado correctamente')
    
    usuario = {
        'nombre': user_name,
        'dni': user_dni
    }
    guardar_usuario(usuario)
    talk(f'Usuario {user_name} guardado correctamente')
    
def guardar_usuario(usuario):
    archivo = "bbdd/usuarios.json"

    # Si el archivo existe, lo cargamos para no perder los datos
    lista_usuarios = []
    
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lista_usuarios = json.load(f)

    # Agregar el nuevo usuario
    lista_usuarios.append(usuario)

    # Guardar todo en el JSON
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)
       
        
def salir():
    talk('Hasta luego. Que tengas un buen día.')
    exit()


def request():
    talk('¿En qué puedo ayudarte?')
    
    stop = False
    while not stop:
        request = audio_to_text().lower()
        if "abrir youtube" in request:
            talk('Abriendo YouTube')
            webbrowser.open('https://www.youtube.com')
        elif 'abrir navegador' in request:
            talk('Abriendo navegador.')
            webbrowser.open('https://www.google.com')
        elif 'qué día es hoy' in request:
            say_day()
        elif 'qué hora es' in request:
            say_hour()
        if "salir" in request:
            salir()
            
    
def say_day():
    day = datetime.date.today()
    weekday = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    talk(f'Hoy es {weekday[day.weekday()]}')    


def say_hour():
    hour = datetime.datetime.now()
    talk(f'En este momento son las {hour.hour} horas y {hour.minute} minutos')


def audio_to_text():
    """
    Convierte el audio en texto.
    """
    # Recognizer
    r = sr.Recognizer()
    
    # Configuramos el micro
    with sr.Microphone() as origin:
        # Tiempo de espera desde que se activa el micro
        r.pause_threshold = 0.8
        
        # Informamos que comienza la grabación
        print('Puedes comenzar a hablar')
        
        # Guardar audio
        audio = r.listen(origin)
        
        try:
            # Buscar en google lo que hemos escuchado
            text = r.recognize_google(audio, language='es-es')
            return text
        except sr.UnknownValueError:
            print('Ups, no te entendí')
            return 'Esperando'
        except sr.RequestError:
            print('Ups, sin servicio')
            return 'Esperando'
        except:
            print('Ups, algo ha salido mal')
            return 'Esperando'

        
def talk(msg):
    """
    Método para que el asistente hable.
    
    :param msg: Mensaje que te va a decir el asistente.
    """
    newVoiceRate = 180
    
    # Encender motor pyttsx3
    engine = pyttsx3.init()
    
    engine.setProperty('voice', 'com.apple.eloquence.es-ES.Monica')
    engine.setProperty('rate', newVoiceRate)
    # Pronunciar mensjaje
    engine.say(msg)
    engine.runAndWait()