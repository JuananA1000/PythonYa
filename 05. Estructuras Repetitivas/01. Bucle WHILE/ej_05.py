'''
  Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a
  7 y cuántos menores.
'''

cont_mas7 = 0
cont_menos7 = 0

x = 1
while x <= 10:
    nota = int(input('Nota %d: ' % x))

    if nota >= 7:
        cont_mas7 += 1
    else:
        cont_menos7 += 1

    x += 1

print('\nNotas >= 7: ', cont_mas7)
print('Notas < 7: ', cont_menos7)
