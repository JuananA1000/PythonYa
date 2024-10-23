'''
  Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un elemento entero, el 
  segundo elemento es una lista de dos elementos etc.
  La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:

  [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
'''

lista = []

for i in range(1, 51):
    elemento = []
    for j in range(1, i + 1):
        elemento.append(j)
    lista.append(elemento)

print(lista)
