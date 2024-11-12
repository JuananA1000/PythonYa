'''
  Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir 
  una li y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas 
  funciones e imprimir el mayor y el menor de la lista.
'''

def return_li(li):
    return li

def return_el_mayor(li):
    mayor = li[0]

    for i in range(1, 5):
        if li[i] > mayor:
            mayor = li[i]
    return mayor

def return_el_menor(li):
    menor = li[0]

    for i in range(1, 5):
        if li[i] < menor:
            menor = li[i]
    return menor

def main():
    lista = []

    print('\nIntroduce 5 números:')
    for i in range(5):
        num = int(input(f'Número [{i + 1}]: '))
        lista.append(num)

    todos = return_li(lista)
    el_mayor = return_el_mayor(lista)
    el_menor = return_el_menor(lista)

    print(f'\nDe la lista: {todos};\nEste es el mayor: {el_mayor}\nEste es el menor: {el_menor}')

main()
