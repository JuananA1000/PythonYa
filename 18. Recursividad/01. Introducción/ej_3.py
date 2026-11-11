'''
  Implementar una función recursiva que imprima en forma descendente de 5 a 1 de uno en uno.
'''

def de_5_a_1(n):
    if n > 0:
        de_5_a_1(n - 1)
        print(n)

de_5_a_1(5)