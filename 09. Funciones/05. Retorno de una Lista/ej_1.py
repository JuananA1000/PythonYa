'''
  Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir
  una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.
'''

def return_lista(li):
    return li

def return_mayor_10(li):
    lista_may_10 = []

    for num in li:
        if num > 10:
            lista_may_10.append(num)

    return lista_may_10

def main():
    lista = []

    for i in range(5):
        numero = int(input(f'Número {i + 1}: '))
        lista.append(numero)

    lista_inicial = return_lista(lista)
    lista_may_10 = return_mayor_10(lista)

    print(f'\nDe la lista: {lista_inicial}\nEstos son los mayores a 10: {lista_may_10}')

main()
