'''
  Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el 
  bloque principal del programa 3 veces con string distintos. 
'''

def cuenta_vocales(str):
    str_min = str.lower()
    contador = 0

    i = 0
    while i < len(str_min):
        if str_min[i] == 'a' or str_min[i] == 'e' or str_min[i] == 'i' or str_min[i] == 'o' or str_min[i] == 'u':
            contador += 1

        i += 1

    print(f'La frase es: "{str}" \ny tiene {contador} vocales')

def main():
    for i in range(3):
        oracion = input(f'\nEscribe una oración [{i + 1}]: ')
        cuenta_vocales(oracion)

main()
