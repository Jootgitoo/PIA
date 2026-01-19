import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1.
ventas_diarias = np.random.randint(100, 1000, 15)
print("Ventas diarias")
print(ventas_diarias)

print("================================")
#2. 
df = pd.DataFrame(
    {
        "dia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "ventas": ventas_diarias
    }
)
print("Dataframe")
print(df)

print("================================")
#3.
# .cumsum() --> suma acumulada, es decir, suma de todas las ventas anteriores hasta ese día
df["ventas_acumuladas"] = df["ventas"].cumsum()
df["objetivo"] = df["ventas"] >= 500

print("Dataframe con ventas acumuladas y objetivo")
print(df)

print("================================")
#4
total_ventas = df["ventas"].sum()
print(f"Total de ventas: {total_ventas}")

dias_exito = len(df[df["objetivo"] == True])
print(f"Dias con objetivo cumplido: {dias_exito}")

dias_exito = (dias_exito / 15) * 100
print(f"Porcentaje de dias con objetivo cumplido: {dias_exito}%")

print("================================")
#5
plt.bar(df["dia"], df["ventas"])
plt.show()

plt.plot(df["dia"], df["ventas_acumuladas"])
plt.show()