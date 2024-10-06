'''
  Cargar por teclado y almacenar en una lista las lista de 5 personas (valores float).
  Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas. 
'''

lista = []

cuantas_personas_altas = 0
cuantas_personas_bajas = 0

for i in range(5):
    altura = float(input(f'Añade altura {i+1}: '))
    lista.append(altura)
    i += 1

promedio = sum(lista) / len(lista)

for altura in lista:
    if altura > promedio:
        cuantas_personas_altas += 1
    elif altura < promedio:
        cuantas_personas_bajas += 1

# Mostrar los resultados
print(f"\nAlturas ingresadas: {lista}")
print(f"Promedio de lista: {promedio:.2f}")
print(f"Personas más altas que el promedio: {cuantas_personas_altas}")
print(f"Personas más bajas que el promedio: {cuantas_personas_bajas}")