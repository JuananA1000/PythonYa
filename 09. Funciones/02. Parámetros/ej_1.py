'''
  Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y 
  nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
'''

def mostrar_mensaje(mensaje):
    print('*************************************************')
    print(mensaje)
    print('*************************************************')

def carga_suma():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    suma = num1 + num2
    print(f'{num1} + {num2} = {suma}')

mostrar_mensaje('El programa calcula la suma de dos valores ingresados por teclado.')
carga_suma()
mostrar_mensaje('Gracias por utilizar este programa')
