import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 
arr_a = np.random.randint(1, 10, 30)
arr_b= np.random.randint(1, 10, 30)
print("Arrays")
print(arr_a)
print(arr_b)
print("========================")

#2. 
df = pd.DataFrame(
    {
        "valor": [arr_a, arr_b],
        "grupo": ["A", "B"]
    }
)
print("Dataframe")
print(df)
print("========================")

#3.  
resultado = df.groupby("grupo")["valor"].apply(lambda x: np.mean(x.iloc[0]))
print(f"Medias: {resultado}")
print("========================")

#4. 
plt.bar(resultado.index, resultado.values)
plt.show()

plt.boxplot([arr_a, arr_b])
plt.show()

#5. 
df.to_csv("src/ejercicio5/datos_grupos.csv", index=False)
df2 = pd.read_csv("src/ejercicio5/datos_grupos.csv")
print(df2)

