'''
  Implementar un método recursivo para ordenar los elementos de una lista.
'''


def ordenar(li, cant):
    if cant > 1:
        for f in range(0, cant-1):
            if li[f] > li[f + 1]:
                aux = li[f]
                li[f] = li[f + 1]
                li[f + 1] = aux
            ordenar(li, cant - 1)


datos = [60, 44, 22, 33, 2]
print(datos)
ordenar(datos, len(datos))
print(datos)
