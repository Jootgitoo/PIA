import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1.
temperaturas = np.random.randint(10, 35, 30)
print("Temperaturas")
print(temperaturas)

print("================================")

#2.
df = pd.DataFrame(
    {
        "dia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        "temperatura": temperaturas
    }
)
print("Dia / Temperatura")
print(df.set_index("dia"))

print("================================")
#3
df["tipo_dia"] = df["temperatura"].apply(lambda x: "frío" if x < 15 else "templado" if 15 <= x <= 25 else "caluroso")
print("Tipo de dia")
print(df.set_index("dia"))

print("================================")
#4
# Agrupamos por 'tipo_dia', seleccionamos la columna 'temperatura' y calculamos la media
media = df.groupby("tipo_dia")["temperatura"].mean()
print(f"Media de temperaturas por tipo de dia: {media}")

print("================================")
#5. 
plt.plot(df['dia'], df['temperatura'])
plt.show()

#Agrupamos por tipo de dia y calculamos la media de cada uno (frio, templado y caluroso)
datos_agrupados = df.groupby('tipo_dia')['temperatura'].mean()

print("Media de temperaturas por tipo de dia")
print(datos_agrupados)

#datos_agrupados.index --> caluroso, frío, templado
#datos_agrupados.values --> media de caluroso, frío, templado
plt.bar(datos_agrupados.index, datos_agrupados.values)
plt.show()