texto = input("Ingrese un texto: ")

menu = (
    "Menú de opciones:\n"
    "1. Ocurrencia letras\n"
    "2. Ocurrencia palabras\n"
    "3. Primera y última palabra del texto\n"
    "4. ¿Aparece la palabra?\n"
)

print(menu)
opcion = int(input("Ingrese una opción (1-4): "))

if opcion == 1:
    letra = input("Ingrese la letra a buscar: ")
    cont = texto.count(letra)
    print(f"La letra '{letra}' aparece {cont} veces en el texto.")
    
elif opcion == 2:
    palabra = input("Ingrese la palabra a buscar: ")
    cont = texto.split().count(palabra)
    print(f"La palabra '{palabra}' aparece {cont} veces en el texto.")
    
elif opcion == 3:
    palabras = texto.split()
    if palabras:
        primera_palabra = palabras[0]
        ultima_palabra = palabras[-1]
    else:
        primera_palabra = ultima_palabra = ""
    print(f"La primera palabra del texto es: '{primera_palabra}' y la última palabra es: '{ultima_palabra}'")
    
elif opcion == 4:
    palabra = input("Ingrese la palabra a buscar: ")
    
    aparece = palabra in texto
    if aparece:
        print(f"La palabra '{palabra}' aparece en el texto.")
    else:    
        print(f"La palabra '{palabra}' no aparece en el texto.")