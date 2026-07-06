"""4. En física de partículas, la precisión de los decimales es crítica. Un sensor de presión
hidráulica en un laboratorio de la universidad entrega una medida de 1024.7689 Pas-
cales como tipo float. Escribe un programa que realice lo siguiente:
a) Defina la variable con el valor del sensor.
b) Convierta dicho valor a un número entero (int), descartando los decimales, y
almacénelo en una variable nueva.
c) Utilice un método propio de Python para redondear el valor original del sensor a
exactamente 2 decimales y guarde el resultado en otra variable.
d ) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
valor truncado como entero y el valor redondeado."""

sensor = 1024.7689
sensor_entero = int(sensor)

print(f"El valor original del sensor es de: {sensor}")
print(f"El valor como numero entero del sensor es de: {sensor_entero}")
print(f"El valor del sensor con dos decimales es de:  {sensor: .2f}")
print(f"El valor redondeado del sensor es de: {round(sensor)}")