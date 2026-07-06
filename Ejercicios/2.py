"""El Departamento de Informática de la Universidad de Los Lagos está monitoreando el consumo de
memoria RAM (en Gigabytes) de uno de sus servidores principales de bases de datos. Se han
registrado los consumos exactos en 4 instantes del día (Mañana, Mediodía, Tarde y Noche) dentro
de una lista de Python.
Escribe un programa en Python que realice las siguientes tareas utilizando exclusivamente lo
aprendido hasta el momento en la Unidad II:
1.Ingresar por terminal los 4 consumos del día y guardarlo en una lista con valores de tipo
decimal (float).
2.Acceder a cada valor individualmente utilizando la indexación de listas para guardarlos en
variables independientes.
3.Calcule y muestre el consumo promedio de RAM del servidor durante el día.
4.Calcule y muestre el 'Rango de Operación' (la diferencia entre el consumo máximo y el mínimo
detectado) haciendo uso de las funciones integradas de Python vistas en clases."""

consumo = []
Consumo_RAM = []
Tiempo = []
print("Ingrese el consumo de RAM en GB para cada instante del día:")
for i in range(4):
    
    monto_consumo = str(input(f"  Momento de el día: "))
    consumo.append(monto_consumo)
    
    monto_consumo_ram = float(input(f"  Valor del consumo de RAM: "))
    Consumo_RAM.append(monto_consumo_ram)

print(f"El promedio de consumo de RAM durante el día es: {sum(Consumo_RAM) / len(Consumo_RAM): .2f}GB")
print(f"El rango de operación (la diferencia entre el consumo máximo y el mínimo) es: {max(Consumo_RAM) - min(Consumo_RAM): .1f}GB")