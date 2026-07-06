"""1. En el análisis de antenas y redes de telecomunicaciones, la impedancia de una linea de
transmisión se compone de una parte real (resistencia) y una parte imaginaria (reac-
tancia). Un ingeniero necesita calcular la impedancia total sumando los componentes
de dos tramos de la red de fibra òptica de la universidad.
a) Defina la impedancia del Tramo 1 como un número complejo con parte real 50 y
parte imaginaria 30 (50 + 30j).
b) Defina la impedancia del Tramo 2 de la misma forma, con parte real 40 y parte
imaginaria -10 (40 - 10j).
c) Calcule la impedancia total sumando ambos tramos.
d ) Muestre en pantalla la impedancia total, y luego imprima por separado solo la
parte real (convertida a número entero int) y la parte imaginaria (convertida a
int) usando los atributos .real y .imag."""

resistencia_tramo_1 = 50
reactancia_tramo_1 = 30

resistencia_tramo_2 = 40
reactancia_tramo_2 = -10

impedancia_tramo_1 = complex(resistencia_tramo_1, reactancia_tramo_1)
impedancia_tramo_2 = complex(resistencia_tramo_2, reactancia_tramo_2)

impedancia_total = impedancia_tramo_1 + impedancia_tramo_2

print("La impedancia total es:", impedancia_total)

parte_real_entera = int(impedancia_total.real)
parte_imaginaria_entera = int(impedancia_total.imag)

print("Parte real (int):", parte_real_entera)
print("Parte imaginaria (int):", parte_imaginaria_entera)