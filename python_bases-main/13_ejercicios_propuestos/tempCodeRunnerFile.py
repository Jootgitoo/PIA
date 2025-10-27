# Ejercicio 5: Juego de Ahorcado
import random

lista_palabras = ["python", "java", "inteligencia", "artificial", "chatgpt"]
palabra_sin_adivinar = []
intentos = 6
letras_dichas = []

palabra = random.choice(lista_palabras) #Elegimos una palabra al azar


for i in palabra: # Añadimos un _ por cada letra de la palabra
    palabra_sin_adivinar.append("_")
    
print() # Salto de línea

while intentos > 0:
    
    print("Palabra: ", end="")
    print(palabra_sin_adivinar)
    print(f"Intentos: {intentos}")
    print(f"Letras dichas: {letras_dichas}")
    print() # Salto de línea
    print("-------------------------")
    print() # Salto de línea
    
    
    letra_a_adivinar = input("Ingresa una letra: ")
    
    if letra_a_adivinar in letras_dichas:
        print("Ya has dicho esa letra. Intenta con otra.")
        continue
            
    
    letras_dichas.append(letra_a_adivinar) # Agrega la letra a la lista

    cont = 0
    for posicion, letra in enumerate(palabra): # enumerate() nos da el índice (posicion) y el valor
        if letra_a_adivinar == letra:
            palabra_sin_adivinar[posicion] = letra_a_adivinar
            cont += 1
    if cont > 0:
        print(f"La letra '{letra_a_adivinar}' está en la palabra")
    else:
        intentos -= 1
        print(f"La letra '{letra_a_adivinar}' no está en la palabra")
        
            
    if "_" not in palabra_sin_adivinar: # Comprobamos si se ha adivinado la palabra
        print("¡Felicidades! Has adivinado la palabra:", palabra)
        exit() # Salimos del programa si se ha adivinado la palabra

print("Has perdido. La palabra era:", palabra)