'''
  Desarrollar un programa que cargue una lista con 10 enteros.
  Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
  Mostrar la lista por pantalla.
  Luego mezclar los elementos de la lista y volver a mostrarlo.
'''

import random

def cargar_lista():
    lista = []
    for i in range(10):
        lista.append(random.randint(0, 1000))

    return lista

def imprimir_lista(lista):
    print(lista)

def mezclar_lista(lista):
    random.shuffle(lista)

    return lista

def main():
    lista = cargar_lista()

    print("\nLista creada:")
    imprimir_lista(lista)

    print("\nLista mezclada:")
    lista = mezclar_lista(lista)
    imprimir_lista(lista)

main()
