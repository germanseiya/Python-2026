"""
Laboratorio 1: 40% de la nota final
Laboratorio 2: 40% de la nota final
Laboratorio 3: 20% de la nota final
1.Solicitar al usuario por terminal el ingreso de las 3 notas individualmente
(estas notas deben n incluir decimales).
2.Almacenar las 3 notas dentro de una estructura de datos de tipo lista.
3.Calcular el promedio ponderado final. Para esto, debes extraer las notas
directamente desde la lista utilizando sus índices (posiciones) y multiplicarlas
por sus respectivos porcentajes antes de sumarlas.
4.Mostrar en la terminal un reporte con todas las notas y el promedio final"""

print("Ingrese sus notas indivivualmente")
notas = [((input("Ingrese la primera nota: ")),
             (input("Ingrese la segunda nota: ")),
                 (input("Ingrese la tercera nota: ")))]
lista_de_notas = list([0,1,2])
ponderacion_1 = 0.40
ponderacion_2 = 0.40
ponderacion_3 = 0.20
promedio = (([0]*ponderacion_1) + ([1] * ponderacion_2) + ([2]*ponderacion_3))
print("Las notas son: ", notas, "y", "el promedio es: ", promedio)