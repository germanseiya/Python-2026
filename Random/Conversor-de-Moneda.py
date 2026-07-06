#Define una constante llamada PI con el valor 3.14159. Crea una variable radio con cualquier valor numérico. Calcula el área del círculo ($Area = PI \cdot radio^2$) e imprime el resultado con un mensaje explicativo.
VALOR_DOLAR = 0.0011

cantidad_pesos = float(input("Ingrese la cantidad de pesos chilenos que desea convertir a dólares: "))
cantidad_dolares = cantidad_pesos * VALOR_DOLAR
print(f"{cantidad_pesos} pesos chilenos equivalen a {cantidad_dolares: .2f} dolares.")