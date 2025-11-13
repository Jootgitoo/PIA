from src.zoomania.entidades import animal, habitat, cuidador
from src.zoomania.gestion import zoologico


def main():
    print("Bienvenido a Zoomania!")

    # Objetos de la clase Habitat
    habitat1 = habitat("Sabana", "Terrestre", 10)
    habitat2 = habitat("Selva", "Terrestre", 15)
    habitat3 = habitat("Acuario", "Acuático", 25)

    
    # Objetos de la clase Animal
    animal1 = animal("Leo", "León", 5, 80, "Sabana")
    animal2 = animal("Molly", "Mono", 3, 50, "Selva")
    animal3 = animal("Dory", "Pez payaso", 2, 30, "Acuario")



    # Objetos de la clase Cuidador
    cuidador1 = cuidador("Ana", "Mañana", [animal1, animal2])
    cuidador2 = cuidador("Luis", "Tarde", [animal3])
    cuidador3 = cuidador("Carla", "Noche", [animal1, animal3])
    
    z = zoologico([animal1, animal2, animal3], [habitat1, habitat2, habitat3], [cuidador1, cuidador2, cuidador3])
    z.mostrar_informacion_zoologico()
    
main()