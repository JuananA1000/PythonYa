'''
  Codificar un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por el palabra 
  "Fizz" y, a su vez, los múltiplos de 5 por "Buzz". Para los números que, al tiempo, son múltiplos de 3 y 5, mostrar el 
  mensaje "FizzBuzz".
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)