import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1.
array = np.random.randint(0, 10, 20) #Generamos 20 int entre 0 y 10
print("Array notas")
print(array)

print("===============================================")

#2.
notas = pd.DataFrame(
    {
        "alumno": ["Alumno1", "Alumno2", "Alumno3", "Alumno4", "Alumno5", "Alumno6", "Alumno7", "Alumno8", "Alumno9", "Alumno10", "Alumno11", "Alumno12", "Alumno13", "Alumno14", "Alumno15", "Alumno16", "Alumno17", "Alumno18", "Alumno19", "Alumno20"],
        "nota": array
    }
)
print("Notas")
print(notas)

print("===============================================")
#3.

notas["aprobado"] = notas["nota"] >= 5
print("Aprobados")
print(notas)

print("===============================================")
#4.
nota_media = notas["nota"].mean()
print(f"Nota media {nota_media}")

nota_max = notas["nota"].max()
print(f"Nota max {nota_max}")

nota_min = notas["nota"].min()
print(f"Nota min {nota_min}")

print("===============================================")
#5.
plt.hist(notas["nota"], bins=20)
plt.ylabel('Notas')
plt.xlabel('Alumnos')
plt.title('Distribución de notas')

media = notas["nota"].mean()
plt.axhline(media, color='r', linestyle='dashed', linewidth=2)

plt.show()
