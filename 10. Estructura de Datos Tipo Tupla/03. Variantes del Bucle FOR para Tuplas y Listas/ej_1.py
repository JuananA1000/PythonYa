'''
  Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
  Luego en otras funciones:

  a) Imprimirla en forma completa.

  b) Obtener y mostrar el mayor.

  c) Mostrar la suma de todas sus componentes.

  Utilizar la nueva sintaxis de for vista en este concepto.
'''

def main():
    lista = []
    for i in range(5):
        num = int(input(f'Ingrese un número[{i+1}]: '))
        lista.append(num)
    return lista

def el_mayor(li):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def suma_lista(li):
    suma = 0
    for i in lista:
        suma += i
    return suma

lista = main()

print("\nLista completa: ", lista)
print("El mayor es: ", el_mayor(lista))
print("La suma de todos los elementos es: ", suma_lista(lista))
