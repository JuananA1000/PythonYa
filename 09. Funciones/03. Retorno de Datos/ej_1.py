'''
  Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.
'''

def superficie(l):
    s = l * l

    return s

def main():
    lado = int(input('Introduce la longitud del lado del cuadrado: '))
    superficie = superficie(lado)

    print(f'La superficie del cuadrado de lado {lado} es {superficie}')

main()
