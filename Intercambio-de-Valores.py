#Declara dos variables, a = 10 y b = 20. Escribe un código que intercambie sus valores de modo que a valga 20 y b valga 10 (puedes usar una variable auxiliar o el truco de asignación múltiple de Python). Imprime ambos resultados para verificar.
a = 10
b = 20
a, b = b, a

print("a es igual a:", a)
print("b es igual a:", b)