'''
  Realizar un programa que lea los lados de n triángulos, e informar:
  
  a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o 
  escaleno (ningún lado igual)
  b) Cantidad de triángulos de cada tipo.
'''


contEQ = 0
contIS = 0
contES = 0

cuantos_triangulos = int(input('Cuántos triángulos: '))

for i in range(cuantos_triangulos):

    print('-- Triángulo [%d] --' % i)
    lado1 = int(input('Lado 1: '))
    lado2 = int(input('Lado 2: '))
    lado3 = int(input('Lado 3: '))

    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        contEQ += 1
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        contES += 1
    else:
        contIS += 1

print(f'De {cuantos_triangulos} analizados:')
print(f'{contEQ} son equiláteros.')
print(f'{contIS} son isósceles.')
print(f'{contES} son escalenos.')
