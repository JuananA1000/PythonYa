'''
  Crear y cargar en un lista los paises de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
  Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de 
  mayor a menor) e imprimir nuevamente.
'''

paises = []
poblacion = []

for i in range(5):
    print(f'Pais [{i + 1}]: ')
    nombre = input(f'Nombre: ')
    habitantes = int(input(f'Habitantes de {nombre}: '))

    paises.append(nombre)
    poblacion.append(habitantes)

for h in range(4):
    for i in range(4):
        if paises[i] > paises[i + 1]:
            aux_not = poblacion[i]
            aux_nom = paises[i]

            poblacion[i] = poblacion[i + 1]
            poblacion[i + 1] = aux_not

            paises[i] = paises[i + 1]
            paises[i + 1] = aux_nom

print('\n--- Paises en orden alfabético ---')
for i in range(5):
    print(f'{paises[i]} --> {poblacion[i]}')

for h in range(4):
    for i in range(4):
        if poblacion[i] < poblacion[i + 1]:
            aux_not = poblacion[i]
            aux_nom = paises[i]

            poblacion[i] = poblacion[i + 1]
            poblacion[i + 1] = aux_not

            paises[i] = paises[i + 1]
            paises[i + 1] = aux_nom

print('\n--- Paises en orden de población ---')
for i in range(5):
    print(f'{paises[i]} --> {poblacion[i]}')
