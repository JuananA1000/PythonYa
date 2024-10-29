'''
  Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres funciones, la primera 
  recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la 
  última recibe la lista y retorna el menor.
'''

def suma(lista):
    suma = 0

    i = 0
    while i < len(lista):
        suma = suma + lista[i]
        i += 1
    return suma

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

    suma_lista = suma(lista)
    print(f'La suma de todos sus elementos es: {suma_lista}.')

    mayor_lista = el_mayor(lista)
    print(f'El mayor de todos sus elementos es: {mayor_lista}.')

    menor_lista = el_menor(lista)
    print(f'El menor de todos sus elementos es: {menor_lista}.')

main()
