'''
  Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga 
  por teclado). Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo primero que 
  se hace es cargar una variable que indique la cantidad de valores a ingresar. Dicha variable se carga antes de entrar 
  a la estructura repetitiva for.
'''

valores_a_ingresar = int(input('Cuantos números: '))
contador = 0

for i in range(valores_a_ingresar):
    n = int(input('Número [%d]: ' % i))

    if n >= 1000:
        contador += 1

print('Valores >= 1000: ', contador)
