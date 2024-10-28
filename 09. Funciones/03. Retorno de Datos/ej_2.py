'''
  Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
'''

def elMayor(num1, num2):

    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2

def main():

    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

    mayor = elMayor(n1, n2)

    print(f'El mayor es {mayor}')

main()
