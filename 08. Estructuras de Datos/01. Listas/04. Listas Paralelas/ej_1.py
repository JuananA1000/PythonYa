'''
  Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga
  por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
'''

nombres = []
edades = []

for i in range(5):
    print(f'Persona [{i+1}]: ')
    nom = input('Nombre: ')
    age = int(input('edad: '))

    nombres.append(nom)
    edades.append(age)

print('\nLos mayores de edad son', end=' ')
for i in range(5):
    if edades[i] >= 18:
        print(nombres[i], end=', ')
