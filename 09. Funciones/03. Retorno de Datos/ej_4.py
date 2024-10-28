'''
  Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.
'''

def calcular_promedio(n1, n2, n3):
    prom = (n1 + n2 + n3) / 3

    return prom

def main():
    num1 = int(input('Introduce número 1: '))
    num2 = int(input('Introduce número 2: '))
    num3 = int(input('Introduce número 3: '))

    promedio = calcular_promedio(num1, num2, num3)
    print(f'\nPROMEDIO: {promedio:.2f}')

main()
