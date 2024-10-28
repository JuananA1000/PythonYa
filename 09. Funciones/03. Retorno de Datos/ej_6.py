'''
  Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros 
  los valores de dos de sus lados: 

  def retornar_superficie(lado1,lado2):

  En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una 
  superficie mayor. 
'''

def retornar_superficie(lado1, lado2):
    sup = lado1 * lado2
    return sup

def main():
    for i in range(2):
        print(f'\nRECTÁNGULO [{i + 1}]')
        l1 = int(input('Introduce lado 1: '))
        l2 = int(input('Introduce lado 2: '))

        superficie = retornar_superficie(l1, l2)

        print(f'\nUn rectángulo de lados {l1, l2} tiene de superficie: {superficie}')

main()
