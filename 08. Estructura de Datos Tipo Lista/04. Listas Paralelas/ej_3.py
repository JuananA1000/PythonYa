'''
  En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:

  a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)

  b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si 
  la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 
  4.
 
  c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”. 
'''

nombres = []
notas = []
calif = ["Insuficiente", "Bueno", "Muy Bueno"]

for i in range(5):
    print(f'EVALUACIÓN [{i+1}]: ')
    nom = input('Nombre: ')
    nota = float(input('Nota: '))

    nombres.append(nom)
    notas.append(nota)

# (ထ, 4)[4, 7][8, 10)
print('\nNOTAS FINALES:')
for i in range(5):
    if notas[i] < 4:
        print(f'{nombres[i]}, tiene un {notas[i]} --> {calif[0]}')
    elif notas[i] >= 4 and notas[i] <= 7:
        print(f'{nombres[i]}, tiene un {notas[i]} --> {calif[1]}')
    elif notas[i] >= 8:
        print(f'{nombres[i]}, tiene un {notas[i]} --> {calif[2]}')
