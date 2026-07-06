"""3. Tres vendedores de una tienda de ropa deportiva registran sus ventas diarias durante 5
días. Los vendedores obtienen un bono por cierta cantidad de ventas realizadas durante
la semana:
Venta semanal total superior a $1.500.000 (Bono de un 20 % del sueldo base)
Venta semanal total superior a $1.000.000 (Bono de un 10 % del sueldo base)
Venta semanal total superior a $500.000 (Bono de un 5 % del sueldo base)
Además considerar: Sueldo Base en Chile 2025 es de $529.000
Se solicita:
a) Crea un diccionario donde la clave sea el nombre del vendedor y el valor otra es-
tructura que guarde las ventas diarias (Puede ser una lista o tupla)
b) Calcula el total de las ventas semanales de cada vendedor y su bono si le corres-
ponde.
c) Obtener el promedio de ventas semanales de cada vendedor.
d) Imprime un reporte con el total del sueldo a pagar por cada vendedor.
Los nombres de los vendedores y los valores de las ventas deben estar instanciado en
código (Hardcodeado)."""

#Martín Aguirre y Germán Cortés

from colorama import init, Fore
init()

SUELDO_BASE = 529000

ventas_vendedores = {
    "Tokai Teiou": [300000, 400000, 250000, 500000, 200000],  
    "Haru Urara": [200000, 150000, 300000, 250000, 200000],  
    "Gold Ship": [100000, 120000, 90000, 110000, 80000]       
}

print(Fore.CYAN + "========================================")
print("       REPORTE DE SUELDOS Y BONOS       ")
print("========================================\n" + Fore.RESET)


for nombre, ventas in ventas_vendedores.items(): 
    
    total_ventas = sum(ventas) 
    promedio_ventas = total_ventas / len(ventas) 
    
    bono = 0
    if total_ventas > 1500000: 
        bono = SUELDO_BASE * 0.20 
    elif total_ventas > 1000000:
        bono = SUELDO_BASE * 0.10 
    elif total_ventas > 500000: 
        bono = SUELDO_BASE * 0.05 
    else:
        bono = 0
        
    sueldo_total = SUELDO_BASE + bono 
    
    print(Fore.GREEN + f"Vendedora: {nombre}" + Fore.RESET)
    print(f"  -> Total Ventas Semanales: ${total_ventas:,}") 
    print(f"  -> Promedio de Venta Diaria: ${promedio_ventas:,}") 
    print(f"  -> Bono Asignado: ${int(bono):,}") 
    print(Fore.YELLOW + f"  -> SUELDO TOTAL A PAGAR: ${int(sueldo_total):,}\n" + Fore.RESET) 

print(Fore.CYAN + "========================================")