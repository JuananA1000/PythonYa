'''
  Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos
  listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
  Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
'''

lista1 = 0
lista2 = 0

print('PRIMERA LISTA\n')
i = 1
while i <= 15:
    num = int(input('Introduce número: '))
    lista1 += num
    i += 1

print('\nSEGUNDA LISTA\n')
j = 1
while j <= 15:
    num = int(input('Introduce número: '))
    lista2 += num
    j += 1


print('\nPrimera Lista: %d' % lista1)
print('Segunda Lista: %d' % lista2)

if lista1 > lista2:
    print('La lista 1 es mayor')
elif lista2 > lista1:
    print('La lista 2 es mayor')
else:
    print('Listas iguales')
