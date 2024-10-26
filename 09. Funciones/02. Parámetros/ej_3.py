'''
  Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su 
  perímetro o su superficie.
'''

def superficie(l):
    s = l * l
    print(f'La superficie de un cuadrado de lado {l} es: {s}')

def perimetro(l):
    p = l * 4
    print(f'El perímetro de un cuadrado de lado {l} es: {p}')

def main():
    lado = int(input('Introduce la longitud del lado del cuadrado: '))
    calculo = input('¿Superficie o perímetro (s / p)?: ')

    if calculo == 's':
        superficie(lado)
    elif calculo == 'p':
        perimetro(lado)
    else:
        print('Error')

main()
