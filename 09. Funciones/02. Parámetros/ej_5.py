'''
  Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar 
  la carga de 3 enteros por teclado y proceder a llamar a la primera función definida. 
'''

def deMenorAMayor(num1, num2, num3):

    print(f'\nNúmeros sin ordenar: {num1} - {num2} - {num3} ')

    if num1 < num2 and num1 < num3:
        if num2 < num3:
            print(f'\nNúmeros ordenados: {num1} - {num2} - {num3}')
        else:
            print(f'\nNúmeros ordenados: {num1} - {num3} - {num2}')
    else:
        if num2 < num3:
            if num1 < num3:
                print(f'\nNúmeros ordenados: {num2} - {num1} - {num3}')
            else:
                print(f'\nNúmeros ordenados: {num2} - {num3} - {num1}')
        else:
            if num1 < num2:
                print(f'\nNúmeros ordenados: {num3} - {num1} - {num2}')
            else:
                print(f'\nNúmeros ordenados: {num3} - {num2} - {num1}')


def main():
    numero1 = int(input('Número [1]: '))
    numero2 = int(input('Número [2]: '))
    numero3 = int(input('Número [3]: '))

    menor, medio, mayor = deMenorAMayor(numero1, numero2, numero3)
    print(f'\nNúmeros ordenados: {menor} - {medio} - {mayor} ')

main()
