"""3. El Departamento de Admisión de la Universidad requiere un script básico para registrar
correos institucionales. El programa debe solicitar al usuario que ingrese su nombre
completo por terminal. Debido a que los usuarios pueden escribir con mayásculas y
minúsculas desordenadas o con espacios de más, el programa debe estandarizar el texto.
Escribe un programa que:
a) Solicite por terminal el nombre del estudiante.
b) Remueva los espacios sobrantes de los extremos.
c) Convierta todo el texto a minúsculas.
d ) Reemplace los espacios intermedios por puntos (.) para simular la estructura de
un correo electrónico.
e) Muestre en pantalla el resultado final con el texto @alumnos.ulagos.cl concatenado
al final."""

input_nombre = input("Ingrese su nombre completo: ")
nombre_estandarizado = input_nombre.strip().lower().replace(" ", ".")
print(nombre_estandarizado + "@alumnos.ulagos.cl")