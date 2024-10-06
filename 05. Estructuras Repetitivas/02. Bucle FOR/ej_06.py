'''
  Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y 
  cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
'''

de3 = 0
de5 = 0

for i in range(10):
    num = int(input('Número [%d]: ' % i))

    if num % 3 == 0:
        de3 += 1

    if num % 5 == 0:
        de5 += 1


print('\nMúltiplos de 3: ', de3)
print('Múltiplos de 5: ', de5)
