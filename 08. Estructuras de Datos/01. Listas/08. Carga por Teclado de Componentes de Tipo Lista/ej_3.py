'''
  Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista. El 
  segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
  Mostrar la lista y la suma de todos sus elementos.
'''

lista = []
n_sublistas = int(input('Cuántas sublistas: '))
n_elementos = int(input('Elementos en cada sublista: '))

for i in range(n_sublistas):
    lista.append([])

    for j in range(n_elementos):
        num = int(input(f'Número [{i}][{j}]: '))
        lista[i].append(num)

    print('\n')

print(f'Tu lista: {lista}')

suma = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        suma += lista[i][j]

print(f'Suma total: {suma}')