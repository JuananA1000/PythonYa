'''
  Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
  Repetir la carga e impresion de la suma 5 veces.
  Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
'''

def suma():
    for i in range(5):
        print(f'Repetición [{i+1}]')
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))

        suma = num1 + num2

        print(f'{num1} + {num2} = {suma}')
        print('------------\n')

suma()
