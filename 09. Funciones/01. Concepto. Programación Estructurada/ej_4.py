'''
  Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del 
  programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva) 
'''

def elMenor():
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    num3 = int(input('Numero 3: '))

    if num1 < num2 and num1 < num3:
        print(f'\n{num1} es el número menor\n')
    elif num2 < num1 and num2 < num3:
        print(f'\n{num2} es el número menor\n')
    else:
        print(f'\n{num3} es el número menor\n')

elMenor()
elMenor()
