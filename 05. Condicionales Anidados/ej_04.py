'''
  Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje
  indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor. 
'''

num = int(input('Ingresa un número: '))

if num >= 0 and num < 10:
    print('Tu número tiene UNA cifra')
elif num >= 10 and num < 100:
    print('Tu número tiene DOS cifras')
elif num >= 100 and num < 1000:
    print('Tu número tiene TRES cifras')
else:
    print('Tu número tiene MÁS dígitos')
