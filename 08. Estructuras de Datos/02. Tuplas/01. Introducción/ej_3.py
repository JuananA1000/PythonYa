'''
  Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar la lista y 
  luego convertir la lista en tupla.
'''

def de_tupla_a_lista(tup):
    lis = list(tup)
    return lis

def de_lista_a_tupla(lis):
    tup = tuple(lis)
    return tup

def main():
    num1 = int(input('\nNúmero 1: '))
    num2 = int(input('Número 2: '))
    num3 = int(input('Número 3: '))

    print(f'\nNormal: {num1}, {num2}, {num3}')

    tupla = (num1, num2, num3)
    pasamos_a_lista = de_tupla_a_lista(tupla)
    print(f'Forma Lista: {pasamos_a_lista}')

    pasamos_a_tupla = de_lista_a_tupla(pasamos_a_lista)
    print(f'Forma Tupla: {pasamos_a_tupla}')

main()
