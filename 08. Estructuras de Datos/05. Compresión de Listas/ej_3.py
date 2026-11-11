'''
  Generar una lista con todos los valores múltiplos de 8 comprendidos entre 1 y 500.
'''

lista_multiplos_8 = [i for i in range(1, 501) if i % 8 == 0]

print(f"Lista de múltiplos de 8 entre 1 y 500: {lista_multiplos_8}")