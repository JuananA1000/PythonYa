'''
  Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla. 
'''

paises = []

for i in range(5):
    pais = input(f'Ingrese pais [{i + 1}]: ')
    paises.append(pais)

print('\nLista sin ordenar: ')
print(paises)

for h in range(4):
    for i in range(4):
        if paises[i] > paises[i + 1]:
            aux = paises[i]
            paises[i] = paises[i + 1]
            paises[i + 1] = aux

print('\nLista de paises alfabéticamente')
print(paises)
