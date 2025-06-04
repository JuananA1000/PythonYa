'''
  Confeccionar un programa que contenga las siguientes funciones:
  a) Carga de una lista de 5 nombres.
  
  b) Ordenar alfabéticamente la lista.
  
  c) Imprimir la lista de nombres
'''

def ordenar_alfabeticamente(li):
    for i in range(4):
        if li[i] > li[i + 1]:
            aux_not = li[i]
            li[i] = li[i + 1]
            li[i + 1] = aux_not

def main():
    lista = []

    for i in range(5):
        nombre = input(f"Ingrese un nombre [{i + 1}]: ")
        lista.append(nombre)

    print(f"\nLista completa: {lista}")
    ordenar_alfabeticamente(lista)
    print(f"\nLista ordenada alfabéticamente: {lista}")

main()
