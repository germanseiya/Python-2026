"""Escriba un programa que Solicite al usuario: 
● Su Nombre y Apellido 
● Su edad (Formateado en ‘Int’) 
● Su carrera 
● Su Estatura (Formateado en ‘Float’) 
Luego el programa debe mostrar toda la información 
en pantalla de manera ordenada y legible."""

from colorama import init, Fore
init()

nombre = input("Ingrese su nombre y su apellido: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
estatura = float(input("Ingrese su estatura: "))

print(Fore.GREEN + "=== DATOS ===")
print("El nombre es: ", nombre)
print("La edad es: ", {edad})
print("La carrera es: ", carrera)
print(f"La estatura es: {estatura} cm")
print("=" *40 + Fore.RESET)