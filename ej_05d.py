'''
  Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene
  uno o dos dígitos.
  (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero) 
'''

num = int(input('Ingresa un número: '))

if num >= 0 and num <= 99:
    print('Tu número tiene uno o dos dígitos')
else:
    print('Tu número tiene MÁS dígitos')
