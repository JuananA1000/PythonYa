'''
   Confeccionar un programa con las siguientes funciones:
   a) Cargar una lista con 5 palabras.
   
   b) Intercambiar la primera palabra con la última.
   
   c) Imprimir la lista 
'''

def cargar_lista():
    lista = []
    print('Ingresa 5 palabras: ')
    for i in range(5):
        lista.append(input(f"Palabra [{i + 1}]: "))
    return lista

def intercambiar(lista):
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

def imprimir_lista(lista):
    for i in lista:
        print(i, end=' ')
    print()

def main():
    lista = cargar_lista()
    lista = intercambiar(lista)
    imprimir_lista(lista)

main()