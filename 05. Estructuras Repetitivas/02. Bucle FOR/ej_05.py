'''
  Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales 
  a 7 y cuántos menores.
'''

cuantos_alumnos = 0

for i in range(10):
    nota = int(input('Nota [%d]: ' % i))
    
    if nota >= 7:
        cuantos_alumnos += 1

print('\nNotas MAYORES o IGUALES a 7: ', cuantos_alumnos)
print('Notas MENORES a 7: ', 10 - cuantos_alumnos)
