""""Un centro de investigación de la Región de Los Lagos registró las
temperaturas de los primeros 3 días de la semana en una lista. Crea un
programa en Python que calcule el promedio de la semana y la
diferencia entre el día más alto y el más bajo usando operaciones de
listas."""

temperatura = [12.5, 14.2, 11.8]
print(f"El promedio de la temperatura semanal es: {sum(temperatura) / len(temperatura): .1f}ºC")
print(f"La diferencia entre la temperatura más alta y la más baja es: {max(temperatura) - min(temperatura): .1f}ºC")