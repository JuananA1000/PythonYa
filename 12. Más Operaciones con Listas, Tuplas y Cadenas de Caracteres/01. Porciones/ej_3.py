'''
  Realizar un programa que contenga las siguientes funciones:
  a) Carga de una lista de 10 enteros.
  
  b) Recibir una lista y retornar otra con la primera mitad (se sabe que siempre llega una lista con una cantidad par de 
  elementos)
  
  c) Imprimir una lista. 
'''

def cargar_lista():
    lista = []
    for i in range(10):
        lista.append(int(input(f'Número [{i + 1}]: ')))
    return lista

def primera_mitad(lista):
    return lista[:len(lista)//2]

def imprimir_lista(lista):
    for i in lista:
        print(i, end=' ')
    print()

def main():
    lista = cargar_lista()
    mitad = primera_mitad(lista)

    print('\nLista original: ', lista)
    print('Primera mitad de la lista: ', end=' ')
    imprimir_lista(mitad)

main()
