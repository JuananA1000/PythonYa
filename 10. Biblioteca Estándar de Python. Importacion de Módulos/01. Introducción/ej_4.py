'''
  Confeccionar una programa con las siguientes funciones:
  a) Generar una lista con 4 elementos enteros aleatorios comprendidos entre 1 y 3. Agregar un quinto elemento con un 1.
  
  b) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a 
  controlar hasta que haya un 1.
  
  c) Imprimir la lista. 
'''

import random

def generar_aleatorio():
    return random.randint(1, 3)

def main():
    lista = []
    for i in range(4):
        lista.append(generar_aleatorio())

    lista.append(1)

    while lista[0] != 1:
        random.shuffle(lista)

    print("Lista: ", lista)

main()