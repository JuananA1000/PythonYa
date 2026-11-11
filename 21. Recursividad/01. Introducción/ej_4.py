'''
  Imprimir los números de 1 a 5 en pantalla utilizando recursividad.
'''

def de_1_a_5(x):
    if x>0:
        de_1_a_5(x-1)
        print(x)

de_1_a_5(5)