'''
  Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro 
  de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
  
  lista=[3, 7, 8, 10, 2]
  multiplicar(lista,3)
'''

def multiplicar(lista, n):
    for i in lista:
        print(i * n)

def main():
    lista = [3, 7, 8, 10, 2]
    multiplicar(lista, 3)

main()
