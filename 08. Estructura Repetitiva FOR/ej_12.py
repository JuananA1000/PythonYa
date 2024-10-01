'''
  Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
  Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se
  pide que se ingrese la cantidad de puntos a procesar.
'''
#        +y |
#           |
#     2     |    1
#           |
# -x  ------ -------  +x
#           |
#     3     |    4
#           |
#        -y |

contP1 = 0
contP2 = 0
contP3 = 0
contP4 = 0
cont00 = 0

cuantos_puntos = int(input('Cuantos puntos analizamos: '))
for i in range(cuantos_puntos):

    print('-- Punto [%d] --' % i)
    x = int(input('Coordenada X: '))
    y = int(input('Coordenada Y: '))

    if x > 0 and y > 0:
        contP1 += 1
    elif x < 0 and y > 0:
        contP2 += 1
    elif x < 0 and y < 0:
        contP3 += 1
    elif x > 0 and y < 0:
        contP4 += 1
    else:
        cont00 += 1

print('\nCONTEO DE PUNTOS')
print('Primer cuadrante: ', contP1)
print('Segundo cuadrante: ', contP2)
print('Tercer cuadrante: ', contP3)
print('Cuarto cuadrante: ', contP4)
print('En Origen: ', cont00)
