"""5. Una plataforma web de la Universidad de Los Lagos mide la velocidad de respuesta
de su servidor de asignación de asignaturas. Se han tomado 3 muestras de tiempo de
respuesta (en milisegundos) de forma manual. Escribe un programa en Python que:
a) Solicite al administrador de la plataforma ingresar por terminal los 3 tiempos de
respuesta (los cuales pueden contener decimales, tipo float).
b) Almacene los 3 valores ingresados dentro de una lista de Python que debe tener
por nombre tiempos respuesta.
c) Acceda por medio de sus índices ([0], [1], [2]) a los elementos de la lista para
calcular el tiempo promedio de respuesta del servidor.
d ) Encuentre el tiempo más rápido (mínimo) y el tiempo más lento (máximo) utili-
zando las funciones propias de Python.
e) Calcule la “brecha de rendimiento”, que corresponde a la resta entre el tiempo
máximo y el mínimo.
f ) Imprima en pantalla la lista completa de datos y el reporte con el promedio y la
brecha calculada."""

consumo = []
Consumo_RAM = []
Tiempo = []
print("Ingrese el consumo de RAM en GB para cada instante del día:")
for i in range(3):
    
    monto_consumo = str(input(f"  Momento de el día: "))
    consumo.append(monto_consumo)
    
    monto_consumo_ram = float(input(f"  Valor del consumo de RAM: "))
    Consumo_RAM.append(monto_consumo_ram)

print(f"El promedio de consumo de RAM durante el día es: {sum(Consumo_RAM) / len(Consumo_RAM): .2f}GB")
print(f"El rango de operación (la diferencia entre el consumo máximo y el mínimo) es: {max(Consumo_RAM) - min(Consumo_RAM): .1f}GB")