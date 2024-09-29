'''
  Una planta que fabrica perfiles de hierro posee un lote de n piezas.
  Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de 
  cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por 
  pantalla la cantidad de piezas aptas que hay en el lote. 
'''

numero_de_piezas = int(input('Numero de piezas: '))
cantidad = 0

x = 1
while x <= numero_de_piezas:
    longitud_perfil = float(input('Longitud perfil (p%d): ' % x))
    if longitud_perfil >= 1.2 and longitud_perfil <= 1.3:
        cantidad += 1
    x += 1

print('Nº piezas aptas: %d' % cantidad)
