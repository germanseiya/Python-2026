colores_primarios = {"Azul", "Rojo", "Amarillo"}
colores_secundarios = set(["Verde", "Naranja", "Violeta"])
print(type(colores_primarios))

print("Conjunto 1: (colores_primarios)")
print("Conjunto 2: (colores_secundarios)")

colores_nuevos = {"Café", "Gris", "Azul", "Rojo", "Azul"}
print("Conjunto 3: (colores_nuevos)")

paciente = {
    'Nombre' : 'Germán Cortés',
    'Edad' : 18,
    'Ciudad' : 'Ancud',
    'Fechas_Atención' : [5, 12, 19],
    'Diagóstico' : 'Resfrio Común'
    
}
print(paciente.keys())
print(paciente.value())
print(paciente.items())

paciente[ 'telefono' ] = '+56937721311'
print(paciente)

print('Nombre' in paciente)
print('Rut' in paciente)

#con copy() se crea una copia independiente del diccionario
paciente2 = paciente.copy()
paciente2['Nombre'] = 'Catalina Gonzáles'
print(paciente['Nombre'])
print(paciente2['Nombre'])
print(paciente2)

medico2 = medico.copy()
print("\n===== DICCIONARIO COPIA (MEDICO2) ==== \N")
print(medico2)
medico2.clear()
print(medico2) = {}