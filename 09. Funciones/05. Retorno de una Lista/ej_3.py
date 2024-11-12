'''
  Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga 
  por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años).
  Imprimir la edad promedio de las personas.
'''

def mayores_edad(li_nom, li_ed):
    mayores = []

    for i in range(len(li_ed)):
        if li_ed[i] >= 18:
            mayores.append(li_nom[i])

    return mayores

def promedio_edades(li_ed):
    prom = sum(li_ed) / len(li_ed)
    
    return prom

def main():
    nombres = []
    edades = []

    for i in range(5):
        print(f'\nPersona {i + 1}')
        nombre = input('Nombre: ')
        edad = int(input('Edad: '))

        nombres.append(nombre)
        edades.append(edad)

    mayores = mayores_edad(nombres, edades)

    print('\nPersonas mayores de edad:', end=' ')
    for nombre in mayores:
        print(nombre, end=' ')

    promedio = promedio_edades(edades)
    print(f'\nLa edad promedio es: {promedio:.2f}')

main()
