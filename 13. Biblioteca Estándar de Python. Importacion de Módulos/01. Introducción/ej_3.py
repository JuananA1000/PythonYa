'''
  Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
  El operador debe tratar de adivinar el número ingresado.
  Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" 
  o "El número aleatorio es menor".
  Mostrar cuando gana el jugador cuantos intentos necesitó.
'''

import random

def generar_aleatorio():
    return random.randint(1, 100)

def main():
    numero_aleatorio = generar_aleatorio()
    intentos = 0

    while True:
        intentos += 1
        numero = int(input("Adivina el número: "))

        if numero == numero_aleatorio:
            print(f"\n¡Ganaste! Has necesitado {intentos} intentos.")
            break
        elif numero < numero_aleatorio:
            print("Mi número es MAYOR.")
        else:
            print("Mi número es MENOR.")

main()
