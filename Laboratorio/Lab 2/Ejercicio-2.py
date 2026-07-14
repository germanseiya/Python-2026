#se le pide al usuario que escriba su código identificado
registro_sucio= input("Escriba su código identificador ")

#se borran los espacios en blanco de los extremos
registro_sin_espacios=(registro_sucio.strip())

#se reemplazan los caracteres de guion bajo (_)
registro_sin_guion_bajo = (registro_sin_espacios).replace("_", "")

#se convierte el texto resultante  letras mayúsculas
registro_limpio = (registro_sin_guion_bajo.upper())

#se despliega en pantalla un reporte del código final y su longitud 
print("El código identificador final y limpio es:", registro_limpio)
print("La longitud de el nuevo código identificador es: ", len(registro_limpio), "caracteres")