import sys
from zoomania.gestion.zoologico import Zoologico
from zoomania.utilidades.excepciones import ZoomaniaError
import csv
import time

def mostrar_menu():
    print("\n--- ZOOMANIA: Sistema de Gestión de Zoológico ---")
    print("1. Agregar Hábitat")
    print("2. Agregar Animal")
    print("3. Agregar Cuidador")
    print("4. Asignar Animal a Hábitat")
    print("5. Alimentar Animal")
    print("6. Ver Informe del Zoológico")
    print("7. Jugar Minijuego: Alimentar a la Bestia")
    print("8. Exportar Informe a CSV")
    print("9. Salir")
    return input("Seleccione una opción: ")

def main():
    zoo = Zoologico()
    
    while True:
        opcion = mostrar_menu()
        
        try:
            if opcion == "1":
                nombre = input("Nombre del hábitat: ")
                tipo = input("Tipo (Selva, Sabana, Acuario, etc.): ")
                capacidad = int(input("Capacidad: "))
                zoo.agregar_habitat(nombre, tipo, capacidad)
                print("Hábitat agregado exitosamente.")

            elif opcion == "2":
                nombre = input("Nombre del animal: ")
                especie = input("Especie: ")
                edad = int(input("Edad: "))
                hambre = int(input("Nivel de hambre inicial (0-100): "))
                zoo.agregar_animal(nombre, especie, edad, hambre)
                print("Animal agregado exitosamente.")

            elif opcion == "3":
                nombre = input("Nombre del cuidador: ")
                turno = input("Turno (Mañana/Tarde/Noche): ")
                zoo.agregar_cuidador(nombre, turno)
                print("Cuidador agregado exitosamente.")

            elif opcion == "4":
                animal = input("Nombre del animal: ")
                habitat = input("Nombre del hábitat: ")
                zoo.asignar_animal_habitat(animal, habitat)
                print("Animal asignado correctamente.")

            elif opcion == "5":
                animal = input("Nombre del animal a alimentar: ")
                zoo.alimentar_animal(animal)
                print(f"{animal} ha sido alimentado.")

            elif opcion == "6":
                print(zoo.generar_informe())

            elif opcion == "7":
                jugar_minijuego(zoo)

            elif opcion == "8":
                exportar_csv(zoo)

            elif opcion == "9":
                print("¡Hasta luego!")
                break
                
            else:
                print("Opción no válida.")

        except ZoomaniaError as e:
            print(f"Error de negocio: {e}")
        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

def jugar_minijuego(zoo):
    print("\n --- MINIJUEGO: ALIMENTAR A LA BESTIA ---")
    print("Tienes 5 segundos para alimentar a todos los animales hambrientos (hambre > 50).")
    print("Escribe el nombre del animal para alimentarlo.")
    
    animales_hambrientos = [a for a in zoo.animales if a.nivel_hambre > 50]
    if not animales_hambrientos:
        print("¡Todos los animales están felices! No hay nada que hacer.")
        return

    print(f"Animales hambrientos: {', '.join([a.nombre for a in animales_hambrientos])}")
    input("Presiona ENTER para empezar...")
    
    start_time = time.time()
    alimentados = 0
    
    while time.time() - start_time < 10 and animales_hambrientos:
        tiempo_restante = 10 - int(time.time() - start_time)
        print(f"Tiempo restante: {tiempo_restante}s")
        
        target = input("Nombre del animal a alimentar: ")
        
        found = False
        for i, animal in enumerate(animales_hambrientos):
            if animal.nombre == target:
                zoo.alimentar_animal(target)
                print("¡Ñam! ")
                del animales_hambrientos[i]
                alimentados += 1
                found = True
                break
        
        if not found:
            print("Ese animal no tiene hambre o no existe.")

        if not animales_hambrientos:
            print("\n¡GANASTE! Has alimentado a todos a tiempo.")
            return

    print("\n¡TIEMPO TERMINADO!")
    if animales_hambrientos:
        print(f"Perdiste. {len(animales_hambrientos)} animales siguen hambrientos y enojados.")
    else:
        print("¡Increíble!")

def exportar_csv(zoo):
    filename = "informe_zoo.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tipo', 'Nombre', 'Detalle1', 'Detalle2'])
        
        for h in zoo.habitats:
            writer.writerow(['Habitat', h.nombre, h.tipo, f"Capacidad: {h.capacidad}"])
            
        for a in zoo.animales:
            writer.writerow(['Animal', a.nombre, a.especie, f"Hambre: {a.nivel_hambre}"])
            
        for c in zoo.cuidadores:
            writer.writerow(['Cuidador', c.nombre, c.turno, '-'])
            
    print(f"Informe exportado a {filename}")

if __name__ == "__main__":
    main()