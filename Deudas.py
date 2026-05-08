# 1. PREPARACIÓN DE LAS "COLUMNAS"
# Creamos listas vacías. En programación, una lista es como una columna de Excel
# que puede crecer todo lo que necesitemos.
cuotas = []
impuestos = []

print("--- SISTEMA DE GESTIÓN DE DEUDAS ---")

# 2. DEFINIR EL LÍMITE (FILAS)
# Esto es como decidir que tu tabla llegará hasta la fila 17.
filas_totales = 17 

# 3. EL BUCLE (EL MOTOR DEL PROGRAMA)
# 'range(1, filas_totales + 1)' le dice a Python que cuente del 1 al 17.
# La variable 'i' irá tomando el valor del número de fila actual.
for i in range(1, filas_totales + 1):
    print(f"\nIngresando datos para la fila {i}:")
    
    # Capturamos el monto de la cuota (Columna A)
    # int() convierte el texto que escribes en un número entero para poder sumarlo.
    monto_cuota = int(input(f"  Valor cuota: "))
    cuotas.append(monto_cuota) # .append() "pega" el valor al final de la lista.
    
    # Capturamos el impuesto (Columna B)
    monto_impuesto = int(input(f"  Valor impuesto: "))
    impuestos.append(monto_impuesto)

# 4. PROCESAMIENTO DE DATOS (LAS FÓRMULAS SUMA)
# sum() es el equivalente exacto a escribir =SUMA(A1:A17) en tu Excel.
total_cuotas = sum(cuotas)      # Esto sería tu celda A18
total_impuestos = sum(impuestos) # Esto sería tu celda B18

# Aquí sumamos los dos resultados anteriores para el gran total.
gran_total = total_cuotas + total_impuestos # Esto sería tu celda C18 (celeste)

# 5. SALIDA DE RESULTADOS (LA VISUALIZACIÓN)
print("\n" + "="*40)
print(f"RESUMEN FINAL (Equivalente a Fila 18)")
print("="*40)
print(f"Total Cuotas (Columna A):   ${total_cuotas:>10}")
print(f"Total Impuestos (Columna B): ${total_impuestos:>10}")
print("-" * 40)
print(f"TOTAL GENERAL (Celda C18):  ${gran_total:>10}")
print("="*40)