zonas_validas = ["Zona Norte", "Zona Centro", "Zona Sur"]
recolectores_autorizados = {"R101", "R102", "R103"}

cosechas_por_zona = {
    'Zona Norte' : [],
    'Zona Centro' : [],
    'zona Sur' : []
}

while True:
    print("\n--- Nueva Entrada de Datos (Escribe 'FIN' en el código para terminar) ---")
    
    recolector = input("Ingrese código de recolector: ").strip()
    if recolector == "FIN":
        break
        
    if recolector not in recolectores_autorizados:
        print("Error: Recolector no autorizado.")
        continue
    
    zona = input("Ingrese nombre de la zona: ").strip()
    if zona not in zonas_validas:
        print("Error: Zona no válida. Use: Zona Norte, Zona Centro o Zona Sur.")
        continue
        
    try:
        peso = float(input("Ingrese peso de la cosecha en kg: "))
        if peso <= 0:
            print("Error: El peso debe ser mayor a 0.")
            continue
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        continue

    cosechas_por_zona[zona].append(peso)
    print(f"¡Datos guardados con éxito para {zona}!")

total_general = 0
zona_maxima = ""
peso_maximo = -1  # Empezamos en -1 para que cualquier suma real sea mayor

print("\n================ REPORTES POR ZONA ================")

for zona, lista_pesos in cosechas_por_zona.items():
    total_zona = sum(lista_pesos)
    total_general += total_zona
    
    cantidad_cosechas = len(lista_pesos)
    if cantidad_cosechas > 0:
        promedio_zona = total_zona / cantidad_cosechas
    else:
        promedio_zona = 0.0
        
    print(f"{zona}: Promedio de cosecha = {promedio_zona:.2f} kg (Total: {total_zona:.2f} kg)")

    if total_zona > peso_maximo:
        peso_maximo = total_zona
        zona_maxima = zona

reporte_maximo = (zona_maxima, peso_maximo)

print("\n================ RESUMEN FINAL ================")
print(f"Total general recolectado en el complejo: {total_general:.2f} kg")
print(f"Tupla de rendimiento máximo (Zona, Total): {reporte_maximo}")