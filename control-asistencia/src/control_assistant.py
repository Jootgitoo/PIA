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
from usuario import Usuario
    
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
    Abre la cámara, muestra una ventana durante 4 segundos y toma la foto automáticamente.
    """
    
    #Accedemos a la cámara
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return None

    #Guardamos el tiempo en el que empieza el proceso para calcular los 4 segundos
    tiempo_inicio = time.time()
    
    #Imagen capturada
    frame = None

    #Controlar si se ha capturado la imagen
    ret = False

    #Mantenemos el bucle abierto hasta 4 segundos
    while (time.time() - tiempo_inicio) < 4:

        #Leemos la imagen de la cámara
        ret, frame = cam.read()
        
        if not ret:
            print("Error: No se pudo leer la imagen de la cámara.")
            break

        #Mostramos la imagen en una ventana
        cv2.imshow("Vista cámara", frame)
        
        #Necesario para que la ventana de OpenCV se refresque y muestre la imagen
        cv2.waitKey(1)

    # Una vez pasados los 4 segundos, cerramos cámara y ventana
    cam.release()
    cv2.destroyAllWindows()

    if not ret or frame is None:
        print("Error: No se pudo capturar la imagen final.")
        return None

    actual_user_image = "fotos/usuario_actual.jpg"
    
    # Guardamos la imagen
    cv2.imwrite(actual_user_image, frame)

    talk(f"Foto inicial capturada")
    comprobar_identidad(actual_user_image, "bbdd/usuarios.json")


def comprobar_identidad(user_image, users_json):
    """
    Comparamos la imagen del usuario con las de la base de datos.
        - Si está registrado accede al programa
        - Si no está registrado se le pide que se registre
    
    :param user_image: Ruta de la imagen del usuario a identificar.
    :param users_json: Ruta del archivo JSON con los datos de los usuarios.
    """

    #Carga el Json
    with open(users_json, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("Datos de usuarios cargados correctamente.")

    #Rutas de las imagenes que se van a utilizar
    list_path_images = [user_image]
    print("Ruta de la imagen del usuario a identificar añadida.")

    #Convertimos el JSON en una lista de objetos Usuario
    list_obj_users = [Usuario(u.get("nombre"), u.get("dni"), u.get("foto")) for u in data["usuarios"]]
    
    #Añadir todas las fotos registradas
    for user in list_obj_users:
        if user.get_foto():
            list_path_images.append(user.get_foto())
    print("Rutas de las imágenes de la base de datos añadidas.")

    fotos = cargar_imagenes(list_path_images)
    print("Imágenes cargadas correctamente.")
    
    fotos = asignar_perfil_color(fotos)
    print("Perfil de color asignado correctamente.")

    try:
        codificaciones = get_cod_faces(fotos)
    except Exception as e:
        print("Error al obtener codificaciones de las caras:", e)
        talk("No se ha detectado una cara válida en alguna de las imágenes. Por favor, inténtalo de nuevo.")
        return
    print("Codificaciones obtenidas correctamente.")

    #Comparamos la foto del usuario con las de la base de datos
    resultados = compare_all_with_control(codificaciones)
    print("Comparación control --> usuarios realizada correctamente.")

    #Buscamos si el usuario está registrado
    usuario_encontrado = False
    
    for i in range(1, len(resultados)):
        if resultados[i]['misma_cara'][0]:
            nombre = list_obj_users[i-1].nombre
            talk(f"Usuario reconocido: Bienvenido {nombre}")
            request()
            
            usuario_encontrado = True
            break
    
    if not usuario_encontrado:
        talk("El usuario no ha sido reconocido. ¿Desea registrarse?")
        request_usr = audio_to_text().lower()
        
        while not "vale" in request_usr:
            talk("No te he entendido. ¿Deseas registrarte? Por favor, responde sí o no.")
            request_usr = audio_to_text().lower()
        
        if "vale" in request_usr:
            registrar_usuario()


def cargar_imagenes(path_list):
    """
    Obtenemos imágenes con las rutas proporcionadas.
    
    :param path_list: Lista de rutas de las imágenes a cargar.
    """

    fotos = []
    for path in path_list:
        fotos.append(fr.load_image_file(path))
    return fotos           

def asignar_perfil_color(fotos_list):
    """
    Asigna el perfil de color RGB a las imágenes cargadas.
    
    :param fotos_list: Lista de imágenes a las que se les asignará el perfil de color.
    """

    for i in range(len(fotos_list)):
        fotos_list[i] = cv2.cvtColor(fotos_list[i], cv2.COLOR_BGR2RGB)
    return fotos_list 

def localizar_cara(fotos_list):
    """
    Localiza la cara en las imágenes proporcionadas.
    
    :param fotos_list: Lista de imágenes en las que se localizará la cara.
    """

    locations = []
    for i in fotos_list:
        locations.append(fr.face_locations(i)[0]) #puede detectar más caras... nos quedamos con la primera
    return locations


def get_cod_faces(fotos_list):
    """
    Obtenemos las codificaciones de las caras en las imágenes proporcionadas.
    
    :param fotos_list: Lista de imágenes en las que se localizará la cara.
    """
    
    cod_faces = []
    for i in fotos_list:
        cod_faces.append(fr.face_encodings(i)[0])
    return cod_faces


def compare_all_with_control(cara_cod_list):
    """
    Comparamos la codificación de la cara con la codificación de control.
    
    :param cara_cod_list: Lista de codificaciones de caras a comparar.
    """
    
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
    """
    Registra un nuevo usuario por voz.
    """
    
    talk('Dime el nombre del usuario')
    user_name = audio_to_text().lower()
    talk('Nombre guardado correctamente')
    
    talk('Dime el dni del usuario')
    user_dni = audio_to_text().lower()
    talk('DNI guardado correctamente')
    
    talk('Vamos a hacerte una foto')
    ruta_foto = tomar_foto_registro(user_name)
    
    usuario = Usuario(user_name, user_dni, ruta_foto)
    guardar_usuario(usuario)
    talk(f'Usuario {user_name} guardado correctamente')
    saludo()

def tomar_foto_registro(nombre):
    """
    Toma una foto
    """
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return ""

    talk("Mantén la mirada en la cámara durante 3 segundos.")
    
    start_time = time.time()
    frame = None
    
    while (time.time() - start_time) < 3:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Registro Usuario", frame)
        cv2.waitKey(1)
        
    cam.release()
    cv2.destroyAllWindows()
    
    if frame is not None:
        ruta = f"fotos/{nombre}.jpg"
        cv2.imwrite(ruta, frame)
        return ruta
    else:
        talk("No se pudo tomar la foto.")
        return ""

def guardar_usuario(usuario):
    """
    Guarda un usuario en el archivo JSON.
    """

    archivo = "bbdd/usuarios.json"

    # Si el archivo existe, lo cargamos para no perder los datos
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"usuarios": []}

    # Agregar el nuevo usuario
    data["usuarios"].append(usuario.get_user())

    # Guardar todo en el JSON
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
       
        
def salir():
    """
    Sale del programa.
    """
    talk('Hasta luego. Que tengas un buen día.')
    exit()


def request():
    """
    Cosas que puede hacer el asistente escuchando al usuario
    """

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
    """
    Dice el día de la semana.
    """
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
    """
    Dice la hora actual.
    """
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