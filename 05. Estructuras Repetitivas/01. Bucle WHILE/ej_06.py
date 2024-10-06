'''
  Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas. 
'''

numero_personas = int(input('Nº Personas: '))
suma_alturas = 0

x = 1
while x <= numero_personas:
    altura = float(input('Altura %d: ' % x))
    suma_alturas += altura
    x += 1

promedio = suma_alturas / numero_personas

print(f'Promedio de alturas: {promedio:.2f}m')
