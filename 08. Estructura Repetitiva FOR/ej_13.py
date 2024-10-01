'''
  Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:

  a) La cantidad de valores ingresados negativos.
  b) La cantidad de valores ingresados positivos.
  c) La cantidad de múltiplos de 15.
  d) El valor acumulado de los números ingresados que son pares.
'''

contPOS = 0
contNEG = 0
contMUL15 = 0
contPAR = 0

for i in range(10):

    num = int(input('Introduce número [%d]: ' % i))
    if num > 0:
        contPOS += 1
    elif num < 0:
        contNEG += 1

    if num % 15 == 0:
        contMUL15 += 1

    if num % 2 == 0:
        contPAR += 1

print('--CONTEO DE NÚMEROS--')
print('Positivos: ', contPOS)
print('Negativos: ', contNEG)
print('Múltiplos de 15: ', contMUL15)
print('Pares: ', contPAR)
