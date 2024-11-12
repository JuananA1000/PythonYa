'''
  Confeccionar un programa que permita:

  a) Cargar una lista de 10 elementos enteros.
  
  b) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
  
  c) Imprimir las dos listas generadas. 
'''

def return_positivos(li):
    positivos = []

    for i in li:
        if i > 0:
            positivos.append(i)

    return positivos

def return_negativos(li):
    negativos = []

    for i in li:
        if i < 0:
            negativos.append(i)

    return negativos

def main():
    lista = []
    cuantos_elementos = 10

    for i in range(cuantos_elementos):
        num = int(input(f'Número [{i+1}]: '))

        lista.append(num)

    lista_pos = return_positivos(lista)
    lista_neg = return_negativos(lista)

    print(f'\nDe la lista: {lista}\nEstos son negativos: {lista_neg}\nY estos positivos: {lista_pos}')

main()