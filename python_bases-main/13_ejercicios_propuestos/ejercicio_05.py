import random

lista_palabras = ["python", "java", "inteligencia", "artificial", "chatgpt"]
palabra_sin_adivinar = []
intentos = 6
letras_dichas = []

palabra = random.choice(lista_palabras) #Elegimos una palabra al azar

print("Palabra: ", end="")

for i in palabra: # Añadimos un _ por cada letra de la palabra
    palabra_sin_adivinar.append("_")
    
print(palabra_sin_adivinar)    

print()


while intentos > 0:
    letra_a_adivinar = input("Ingresa una letra: ")
    
    letras_dichas.append(letra_a_adivinar) # Agrega la letra a la lista

    cont = 0
    for letra in palabra:
        if letra_a_adivinar == letra:
            palabra_sin_adivinar[palabra.index(letra)] = letra_a_adivinar
            cont += 1
    if cont > 0:
        print(f"La letra '{letra_a_adivinar}' está en la palabra.")
    else:
        intentos -= 1
        print(f"La letra '{letra_a_adivinar}' no está en la palabra")
            
    print("Palabra: ", end="")
    print(palabra_sin_adivinar)
    print(f"Intentos: {intentos}")
    print(f"Letras dichas: {letras_dichas}")
