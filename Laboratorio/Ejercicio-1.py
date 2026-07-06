#Se le solicita al usuario que ingrese las muestras  
registro_lluvia = []
for i in range (5):
    registro_lluvia = float(input("Ingrese las cinco muestras meteorológicas "))

#traté de hacer que el número decimal pase a número entero porque 
registro_lluvia_entero = int(registro_lluvia)
promedio_registro_lluvia = sum(registro_lluvia_entero)

#Se imprime la lista completa de datos
print("El registro de la lluvia es: ", )
print("El promedio calculado es :", promedio_registro_lluvia)