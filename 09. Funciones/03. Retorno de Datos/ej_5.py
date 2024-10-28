'''
  Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado. 
'''

def calcular_perimetro(l):
    p = l * 4
    return p

def main():
    lado = int(input('Introduce la longitud del lado del cuadrado: '))
    perimetro = calcular_perimetro(lado)

    print(f'El perímetro de un cuadrqado de lado {lado} es {perimetro}')

main()
