from colorama import init, Fore
init()

edad = 15
num = 0

#while edad > 18:
#    print("Eres menor de edad, no puedes manejar")

#while True:
#    print(num)
#    num = num + 2

while num <= 100:
    print(num)
    num = num + 2
print(Fore.GREEN + "Cuarto bucle terminado")

while num <= 200:
    print(num)
    num = num +2
else:
    print("Mi condición es mayor a 200")
print(Fore.CYAN + "Quinto bucle terminado")

while num <= 300:
    print(num)
    num = num +2
    if num == 250:
        print("Mi  condición es igual a 250")
print(Fore.BLUE + "Sexto bucle terminado")

while num <= 400:
    print(num)
    num = num +2
    if num == 350:
        print(Fore.BLACK + "Se detiene el bucle")
        break
print(num)
print(Fore.GREEN + "Septimo bucle terminado")

num = 0
while num <= 49:
    print(num)
    num = num + 1
    if num == 40:
            continue
    print(num)
print(Fore.YELLOW + "Octavo bucle termindado")

print(Fore.GREEN + "=== Bucle FOR ===")
for i in range (1,2,3,4,5,6,7,8,9,10):
    print(i)
listita = [1,2,3,4,5,6,7,8,9,10]

print(Fore.GREEN + "\n2=== Bucle FOR ===")
for i in listita:
    print(i)

print(Fore.GREEN + "\n3=== Bucle FOR ===")
for i in range(1,101):
    print(i)