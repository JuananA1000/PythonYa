'''
  Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y
  nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
  Implementar estas actividades en tres funciones.
'''

# Declaración de funciones
def presentacion():
    print('\nPrograma suma dos valores introducidos por teclado.')
    print('-------------------------------')

def suma():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    suma = num1 + num2

    print(f'\n{num1} + {num2} = {suma}\n')

def fin():
    print('¡¡AGUR MINGA FRÍA!!')
    print('-------------------------------')

# Llamada a las funciones
presentacion()
suma()
fin()
