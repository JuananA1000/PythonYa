'''
  Definir una función que cargue una lista con palabras y la retorne.
  Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.
'''

def cargar_lista():
    lista = []
    for i in range(5):
        palabra = input(f'Ingrese una palabra[{i+1}]: ')
        lista.append(palabra)
    return lista

def palabras_con_mas_de_5_caracteres(lista):
    print("\nPalabras con más de 5 caracteres:", end=" ")
    for i in lista:
        if len(i) > 5:
            print(i, end=", ")

lista = cargar_lista()
palabras_con_mas_de_5_caracteres(lista)
