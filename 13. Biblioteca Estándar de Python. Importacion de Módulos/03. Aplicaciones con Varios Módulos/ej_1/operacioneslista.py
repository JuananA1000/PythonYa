def cargar():
    lista = []
    for x in range(5):
        valor = int(input(f"Ingrese valor [{x + 1}]: "))
        lista.append(valor)
    return lista

def imprimir_mayor(lista):
    may = lista[0]
    for x in range(1, 5):
        if lista[x] > may:
            may = lista[x]
    print("\nMayor de la lista: ", may)

def imprimir_suma(lista):
    suma = 0
    for elemento in lista:
        suma = suma+elemento
    print("Suma de todos sus elementos: ", suma)