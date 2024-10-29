'''
  Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno 
  con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
  En el bloque principal iniciamos por asignación la lista de string:
  
  palabras=['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
  print('Palabra con mas caracteres:',mascaracteres(palabras))
'''

def mas_caracteres(lista):

    palabra_mayor = lista[0]
    for palabra in lista:
        if len(palabra) > len(palabra_mayor):
            palabra_mayor = palabra

    return palabra_mayor

def main():
    palabras = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
    print('Palabra con más caracteres:', mas_caracteres(palabras))

main()