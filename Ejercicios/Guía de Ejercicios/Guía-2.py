"""2. Al desarrollar sistemas informáticos, los usuarios suelen ingresar datos con espacios
accidentales o formatos incorrectos. El sistema de la biblioteca de la ULagos recibió el
RUT de un estudiante, pero viene “sucio” con espacios al inicio, al final y con puntos
intermedios: “ 19.543.872-K ”...
Escribe un programa que:
a) Guarde el RUT original en una variable de tipo string.
b) Utilice el método propio de Python para eliminar los espacios en blanco de los
extremos.
c) Utilice un método propio de Python para eliminar los puntos (.).
d ) Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
resultado por pantalla junto al RUT con su nuevo formato."""

rut_original = " 19.543.872-k "

rut_sin_espacios = rut_original.strip()
print(rut_sin_espacios)

rut_limpio = rut_sin_espacios.replace(".", "")
print(rut_limpio)

largo_rut = len(rut_limpio)
print(f"El largo del RUT limpio es: {largo_rut} y el RUT con nuevo formato es: {rut_limpio}")