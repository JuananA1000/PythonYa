'''
  Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.
'''

def imprimir_lista(li):

    for i in range(len(li)):
        print(li[i], end=' ')

def main():
    lista = []

    print('\nIntroduce 10 números:')
    for i in range(10):
        num = int(input(f'Número [{i + 1}]: '))
        lista.append(num)

    print('\nLista: ', end='')
    todos = imprimir_lista(lista)

    return todos

main()
