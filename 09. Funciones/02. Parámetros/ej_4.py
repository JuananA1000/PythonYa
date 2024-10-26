'''
  Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el 
  bloque principal del programa 3 veces con string distintos. 
'''

def cuentaVocales(str):
    str_min = str.lower()
    cuenta_vocales = 0

    i = 0
    while i < len(str_min):
        if str_min[i] == 'a' or str_min[i] == 'e' or str_min[i] == 'i' or str_min[i] == 'o' or str_min[i] == 'u':
            cuenta_vocales += 1

        i += 1

    print(f'La frase es: "{str}" \ny tiene {cuenta_vocales} vocales')

def main():
    for i in range(3):
        oracion = input(f'\nEscribe una oración [{i + 1}]: ')
        cuentaVocales(oracion)

main()
