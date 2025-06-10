'''
  Confeccionar un programa que contenga las siguientes funciones:
  a) Carga de una lista y retorno al bloque principal.
 
  b) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
 
  c) Imprimir la lista 
'''

def fijar_cero(li):
    for i in range(len(li)):
        if li[i] < 10:
            li[i] = 0

def main():
    lista = []
    continua = "s"

    while continua == "s":
        num = int(input("Ingrese un número: "))
        lista.append(num)
        continua = input("Desea continuar[s/n]?: ")

    print(f"\nLista completa: {lista}")
    fijar_cero(lista)
    print(f"\nLista con elementos a cero: {lista}")

main()
