'''
  Confeccionar un programa con las siguientes funciones:

  a) Cargar una lista de 5 enteros.

  b) Retornar el mayor y menor valor de la lista mediante una tupla.

  Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
'''

def return_max_y_min(li):
    mayor = max(li)
    menor = min(li)

    return (mayor, menor)

def main():
    lista = []

    print('Ingrese 5 números enteros:')
    for i in range(5):
        numero = int(input(f'Número {i+1}: '))
        lista.append(numero)

    mayor, menor = return_max_y_min(lista)

    print(f'\nLista ingresada: {lista}')
    print(f'El mayor es: {mayor}')
    print(f'El menor es: {menor}')

main()
