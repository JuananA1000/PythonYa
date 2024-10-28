'''
  Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por 
  teclado.
'''

def el_mayor(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        print(f'\n{num1} es el número mayor\n')
    elif num2 > num1 and num2 > num3:
        print(f'\n{num2} es el número mayor\n')
    else:
        print(f'\n{num3} es el número mayor\n')

def main():

    print('\n...Ejecutando función main()\n')
    v1 = int(input('Numero 1: '))
    v2 = int(input('Numero 2: '))
    v3 = int(input('Numero 3: '))

    el_mayor(v1, v2, v3)

main()
