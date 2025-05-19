'''
  En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor 
  la cantidad de habitantes. Implementar una función para mostrar cada clave y valor.
'''

def main(paises):
    for pais in paises:
        print(f'{pais}: {paises[pais]}')

paises = {"ARG": 45000000, "ESP": 47000000, "CHI": 19000000}
main(paises)
