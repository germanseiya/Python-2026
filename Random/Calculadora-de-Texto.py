#Pide al usuario que ingrese dos números mediante la función input(). Ten en cuenta que input() recibe el dato como un string (str). Convierte esos valores a enteros (int), súmalos y luego muestra el resultado final convertido nuevamente a texto dentro de una frase que diga: "La suma total es: [resultado]".
# 1. Solicitamos los datos (recuerda que input() siempre devuelve un string)
numero1_texto = input("Ingresa el primer número: ")
numero2_texto = input("Ingresa el segundo número: ")

# 2. Convertimos los textos a números decimales (float) para poder operarlos
# Usamos float() por si decides ingresar números como 10.5
num1 = float(numero1_texto)
num2 = float(numero2_texto)

# 3. Realizamos la operación lógica
suma = num1 + num2

# 4. Mostramos el resultado usando una f-string (como en tus ejercicios anteriores)
# Usamos :.2f para que no te salgan esos decimales infinitos que vimos antes
print(f"La suma total entre {num1} y {num2} es: {suma:.2f}")