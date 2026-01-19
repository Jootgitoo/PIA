## Ejercicio 2: Temperaturas diarias

1. Genera con **NumPy** 30 temperaturas aleatorias entre 10 y 35 (un mes).
2. Crea un DataFrame con:
    - `dia` (1 a 30)
    - `temperatura`
3. Añade una columna `tipo_dia`:
    - `"frío"` si < 15
    - `"templado"` si 15–25
    - `"caluroso"` si > 25
4. Calcula la temperatura media por tipo de día.
5. Dibuja con **Matplotlib**:
    - Un gráfico de líneas de la temperatura diaria
    - Un gráfico de barras con la temperatura media por tipo de día