"""2. Construir un programa que calcule e imprima la sumatoria:
S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800"""

from colorama import init, Fore
init()

num1 = 500
num2 = 456
suma_total = 0

print(Fore.GREEN + "-"*40)
while num1 <= 800:
    print(num1)
    suma_total = suma_total + num1 
    num1 = num1 + 10
    if num1 == 800:
        suma_total = suma_total + num1 
        break
print(f"{num1}")
print(Fore.GREEN + "-"*40)

print("\n")

print(Fore.YELLOW + "-"*40)
while num2 <= 456:
    print(num2)
    suma_total = suma_total + num2 
    num2 = num2 - 2
    if num2 == 398:
        suma_total = suma_total + num2
        break
print(f"{num2}")
print(Fore.YELLOW + "-"*40)

print(Fore.CYAN + f"La suma total es {suma_total}")