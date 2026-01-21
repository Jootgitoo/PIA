import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 
arr = np.random.randint(150, 200, 50)
print("Alturas")
print(arr)
print("========================")

#2. 
df = pd.DataFrame(arr, columns=["altura"])
print("Dataframe")
print(df)
print("========================")

#3 
media_altura = arr.mean()
print(f"Media: {media_altura}")

mediana_altura = np.median(arr)
print(f"Mediana: {mediana_altura}")

desviacion_estandar = arr.std()
print(f"Desviacion estandar: {desviacion_estandar}")

print("========================")

#4 

df["grupo"] = df["altura"].apply(lambda x: "baja" if x < media_altura else "alta")
print(df)
print("========================")

#5 

plt.hist(df["altura"], bins=20)
plt.ylabel("Frecuencia")
plt.xlabel("Altura (cm)")
plt.axvline(media_altura, color="red", linestyle="dashed", linewidth=2)
plt.show()