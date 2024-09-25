'''
  Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad. 
'''

dia = int(input('Ingresa un número de día: '))
mes = int(input('Ingresa un número de mes: '))
año = int(input('Ingresa un número de año: '))

if dia == 25 and mes == 12:
    print('¡¡¡ES NAVIDAD!!!')
else:
    print('No es navidad')
