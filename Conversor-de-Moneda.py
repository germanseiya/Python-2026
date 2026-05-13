VALOR_DOLAR = 0.0011

cantidad_pesos = float(input("Ingrese la cantidad de pesos chilenos que desea convertir a dólares: "))
cantidad_dolares = cantidad_pesos * VALOR_DOLAR
print(f"{cantidad_pesos} pesos chilenos equivalen a {cantidad_dolares: .2f} dolares.")