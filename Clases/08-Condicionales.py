from colorama import init, Fore
init()

print(Fore.YELLOW + 'Texto Amarillo')

licencia = False
automovil = True
edad = 19

if licencia and edad >= 18:
    print(Fore.GREEN + "Puede conducir un automovil ya que es mayor de edad")
else:
    print(Fore.RED + "No puede conducir un automovil ya que es menor de edad")

if licencia and edad >= 18:
    print(Fore.GREEN + "Puede conducir un automovil ya que es mayor de edad")
elif automovil:
    print(Fore.YELLOW + "Puede conducir un automovil, pero no tengo licencia")
else:
    print(Fore.RED + "No puedo conducir un automovil ya que no tengo ni la edad ni licencia de conducir")