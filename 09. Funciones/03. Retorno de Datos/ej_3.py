'''
  Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. 
  En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el 
  bloque principal cual de las dos palabras tiene más caracteres.
'''

def cantidad_de_caracteres(str):
    return len(str)

def main():
    for i in range(2):
        frase = input(f'\nEscribe una frase [{i + 1}]: ')
        n_caracteres = cantidad_de_caracteres(frase)

        print(f'Tu frase es: "{frase}"\ny tiene {n_caracteres} caracteres.')

main()
