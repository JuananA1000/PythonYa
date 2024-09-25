'''
  Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y
  (distintos a cero).
  Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
  (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.) 
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

x = int(input('Coordenada X: '))
y = int(input('Coordenada Y: '))

if x > 0 and y > 0:
    print('(%d, %d): Primer cuadrante' % (x, y))
elif x < 0 and y > 0:
    print('(%d, %d): Segundo cuadrante' % (x, y))
elif x < 0 and y < 0:
    print('(%d, %d): Tercer cuadrante' % (x, y))
elif x > 0 and y < 0:
    print('(%d, %d): Cuarto cuadrante' % (x, y))
else:
    print('(%d, %d): Origen' % (x, y))
