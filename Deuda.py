i = 1
resumen = 0
print("¿cuantos dias le debe?")
dias=int(input("... "))
while i <= dias:
    monedas=int(input("ingrese valor de cada dia, "))
    resumen = monedas + resumen
    impuesto = dias * 100
    impuesto1 = impuesto * dias
    i = i + 1
print("valor total ",resumen,"valor del impuesto", impuesto, "valor del impuesto ya calculado ",impuesto1)
total = resumen + impuesto1
print("lo que da de valor", total)