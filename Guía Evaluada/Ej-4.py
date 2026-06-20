"""Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por
Nicómaco de Gerasa:
Sumando el primer impar, se obtiene el primer cubo.
Sumando los dos siguientes impares, se obtiene el segundo cubo
Sumando los tres siguientes, se obtiene el tercer cubo, y así sucesivamente.
Ejemplo:
1³ = 1 = 1
2³ = 3 + 5 = 8
3³ = 7 + 9 + 11 = 27
4³ = 13 + 15 + 17 + 19 = 64
Imprimir por pantalla, los primeros n cubos, considerando el valor de n obtenido desde
teclado."""

from colorama import init, Fore
init()

n = int(input("Ingrese la cantidad de cubos a generar: "))
impar_actual = 1

for i in range(1, n + 1):
    suma_cubo = 0
    impares_del_grupo = []
    for j in range(i):
        suma_cubo = suma_cubo + impar_actual
        impares_del_grupo.append(str(impar_actual))
        impar_actual = impar_actual + 2
        texto_suma = " + ".join(impares_del_grupo)
    print(f"{i}³ = {texto_suma} = {suma_cubo}")