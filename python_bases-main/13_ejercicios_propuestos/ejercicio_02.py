name = input("Nombre del producto: ")
category = input("Categoría del producto: ")
price = float(input("Precio del producto: "))

if category == "Telefonía":
    price = price - (price * 0.15)
elif category == "Informática":
    price = price - (price * 0.18)
else:
    price = price - (price * 0.22)


print(f"El precio final del producto es: {price:.2f}€")