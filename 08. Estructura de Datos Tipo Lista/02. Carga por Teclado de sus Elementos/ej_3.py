'''
  Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.
'''

lista = []

for i in range(5):      
    sueldo = float(input(f'Añade sueldo {i+1}: '))
    lista.append(sueldo)
    i += 1

promedio = sum(lista) / len(lista)

print(f'Lista de sueldos: {lista}\nPromedio de sueldos: {promedio}')
