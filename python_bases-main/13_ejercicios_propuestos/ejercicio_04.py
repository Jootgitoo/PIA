
menu = "\nBienvendo a su cajero automático\n Seleccione un opción: \n 1. Consultar saldo \n 2. Ingresar dinero \n 3. Retirar dinero \n 4. Salir"
saldo = 1000
salir = False

while not salir:
    
    opcion = input(menu + "\nIngrese una opción: ")
    
    match opcion:
        
        case "1":
            print(f"\nSu saldo es de {saldo}€\n")
            
        case "2":
            saldo += float(input("\nIngrese la cantidad a ingresar: "))
            print(f"Deposito realizado. Su saldo actual es: {saldo}€ \n")
            
        case "3":
            saldo_a_retirar = float(input("\nIngrese la cantidad a retirar: "))
            
            if saldo_a_retirar > saldo:
                print("\n\nNo tiene suficiente saldo para realizar el retiro.\n")
            else:
                saldo -= saldo_a_retirar
                print(f"Retiro realizado. Su saldo actual es: {saldo}€ \n")
            
        case "4":
            salir = True
            print("\n\nGracias por usar el cajero automático. ¡Hasta luego!")