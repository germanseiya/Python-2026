"""1. Contar las repeticiones de una palabra en una tupla:
“El Proyecto Integrador del primer semestre, se evaluará y desarrollará en 3 asignaturas en con-
junto: Taller de Introducción a la Ingeniería donde trabajarán el desarrollo práctico del proyecto,
Habilidades Comunicativas donde desarrollarán las habilidades de presentación y redacción y por
último Programación, donde aplicarán técnicas para codificar y diseñar el software del proyecto.”
a) Lea el párrafo. Este debe ser ingresado por teclado.
b) Separe sus palabras y debe guardarlas en una lista.
c) Solicite al usuario una palabra a buscar.
d) Imprima cuántas veces aparece dicha palabra (Debe ser sensible a mayúsculas y
minúsculas).
Requisito especial: Si el párrafo está vacío, debe lanzar y capturar una excepción (Va-
lueError) indicando “El texto no puede estar vacío”."""

#Martín Aguirre y Germán Cortés

parrafo = input("ingrese un párrafo: ").strip()
try:
    if not parrafo:
        raise ValueError("El texto no puede estar vacío")
    
    palabras = tuple(parrafo.split())
    palabra_a_buscar = input("Ingrese la palabra a buscar: ")
    contador = palabras.count(palabra_a_buscar)
    print(f"La palabra '{palabra_a_buscar}' aparece {contador} veces en el parrafo.")
except ValueError as e:
    print(e)
    exit()