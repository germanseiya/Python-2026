from colorama import init, Fore
init()

print(Fore.GREEN + "=== MENÚ ===")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo Italiano")
opción = input("Por favor, elige una opcion (1-3): " + Fore.RESET)

match opción:
    case "1":
        print("Has elegido una Hamburguesa. Precio: $4000")
    case "2":
        print("Has elegido una Pizza. Precio: $7500")
    case "3":
        print("Has elegido un Completo Italiano. Precio: $2500")
    case "_":
        print("Por favor seleccione una opción correcta")


mes = int(input(Fore.YELLOW + "Ingrese un mes: "))
match mes:
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera" + Fore.RESET)