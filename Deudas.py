cuotas = []
impuestos = []

print("--- SISTEMA DE GESTIÓN DE DEUDAS ---")

filas_totales = 17 

for i in range(1, filas_totales + 1):
    print(f"\nIngresando datos para la fila {i}:")
    
    monto_cuota = int(input(f"  Valor cuota: "))
    cuotas.append(monto_cuota)
    
    monto_impuesto = int(input(f"  Valor impuesto: "))
    impuestos.append(monto_impuesto)

total_cuotas = sum(cuotas)
total_impuestos = sum(impuestos)

gran_total = total_cuotas + total_impuestos

print("\n" + "="*40)
print(f"DEUDA FINAL")
print("="*40)
print(f"Total Cuotas:   ${total_cuotas:>10}")
print(f"Total Impuestos: ${total_impuestos:>10}")
print("-" * 40)
print(f"DEUDA TOTAL:  ${gran_total:>10}")
print("="*40)