'''
  Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que 
  imprima el mayor y el menor valor de la lista.
'''

def el_mayor(lista):
    mayor = lista[0]

    for i in range(1, 5):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def el_menor(lista):
    menor = lista[0]

    for i in range(1, 5):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def main():
    lista = [10, 7, 3, 7, 2]

    print(f'\nDada esta lista: {lista}.')

    mayor_lista = el_mayor(lista)
    print(f'El mayor de todos sus elementos es: {mayor_lista}.')

    menor_lista = el_menor(lista)
    print(f'El menor de todos sus elementos es: {menor_lista}.')

main()
