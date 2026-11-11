'''
  Definir dos listas de 3 elementos.
  La primera lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
  La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin
  hijos.
  Imprimir los nombres del padre, la madre y sus hijos.
  También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.

  Un ejemplo si se define por asignación:

  padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
  hijos=[["marcos","alberto","silvia"], [], ["oscar"]]

  Como son listas paralelas podemos decir que la familia cuyos padres son "juan" y "ana" tiene tres hijos llamados
  "marcos", "alberto", "silvia". La segunda familia no tiene hijos y la tercera tiene solo uno.
'''

padres = []
hijos = []

for i in range(3):
    print(f'\nFamilia [{i + 1}]: ')
    papa = input(f'Nombre del padre: ')
    mama = input(f'Nombre de la madre: ')
    cuantos_hijos = int(input(f'Cuántos hijos: '))

    lista_hijos = []
    if cuantos_hijos > 0:
        for j in range(cuantos_hijos):
            hijo = input(f'Hijo [{j + 1}]: ')
            lista_hijos.append(hijo)

    padres.append([papa, mama])
    hijos.append(lista_hijos)

print('\n--- FAMILIAS ---')
for i in range(3):
    padre = padres[i][0]
    madre = padres[i][1]

    print(f'\nFamilia [{i + 1}]: ')
    if hijos[i]:
        print(f'{padre} y {madre} son padres de: {hijos[i]}')
    else:
        print(f'{padre} y {madre} no tienen chiquillos.')
