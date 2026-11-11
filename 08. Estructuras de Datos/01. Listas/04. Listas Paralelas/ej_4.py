'''
  Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercera 
  lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista. 
'''

lista1 = []
lista2 = []
lista_res = []

for i in range(4):
    print('-- Lista 1 -- ')
    num1 = int(input('Número [%d]: ' % i))

    print('-- Lista 2 -- ')
    num2 = int(input('Número [%d]: ' % i))

    lista1.append(num1)
    lista2.append(num2)

for i in range(4):
    suma = lista1[i] + lista2[i]
    lista_res.append(suma)

print('\nLista 1: ', lista1)
print('Lista 2: ', lista2)
print('Resultado: ', lista_res)
