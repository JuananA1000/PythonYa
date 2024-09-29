'''
  Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno 
  en uno.
  
  Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.
'''

limite = int(input('Ingresa un límite: '))

x = 1
while x <= limite:
    print(x, end=' ')  # Evitar salto de línea
    x += 1
