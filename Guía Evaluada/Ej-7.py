"""7. Determinar el factorial de un número n, donde:
n! = n · (n - 1) · (n - 2)..,3 · 2 · 1

factorial(x) = 1                     si x = 0
               x · factorial(x - 1)  si x ≥ 1"""

#Martín Aguirre y Germán Cortés

from colorama import init, Fore
init()

def calcular_factorial(x):
    if x == 0:
        return 1
    else:
        return x * calcular_factorial(x - 1)

print(Fore.CYAN + "========================================")
print("         CÁLCULO DE FACTORIALES         ")
print("========================================\n" + Fore.RESET)

while True:
    n = int(input("Ingrese un número entero positivo (n): "))
    if n >= 0:
        break
    else:
        print(Fore.RED + "Error: El número debe ser mayor o igual a 0.\n" + Fore.RESET)

resultado = calcular_factorial(n)

print(Fore.GREEN + f"\nEl factorial de {n} ({n}!) es: {resultado:,}" + Fore.RESET)
print(Fore.CYAN + "========================================")