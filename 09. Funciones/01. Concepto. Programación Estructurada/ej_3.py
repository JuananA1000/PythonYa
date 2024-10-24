'''
  Desarrollar un programa con dos funciones. La primera solicite el ingreso de un entero y muestre el cuadrado de dicho 
  valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del 
  programa principal a ambas funciones. 
'''

def cuadrado():
    print('CUADRADOS')
    num1 = int(input('Número: '))

    cuadrado = pow(num1, 2)

    print(f'\nEl cuadrado de {num1} es {cuadrado}\n')

def prod():
    print('PRODUCTOS')
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    prod = num1 * num2

    print(f'\n{num1} * {num2} = {prod}\n')

cuadrado()
prod()
