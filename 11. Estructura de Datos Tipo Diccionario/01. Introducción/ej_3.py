'''
  Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y 
  el valor es la palabra en castellano.

  Crear las siguientes funciones:
  a) Cargar el diccionario.
  
  b) Listado completo del diccionario.
    
  c) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción. 
'''

def main():
    diccionario = {}
    continua = "s"
    i = 0

    while continua == "s":
        print(f"\nAcepción [{i+1}]")
        esp = input("Palabra ESP: ")
        ing = input("Palabra ING: ")
        diccionario[ing] = esp
        continua = input("Quiere cargar otra palabra[s/n]: ")

    return diccionario

def imprimir(diccionario):
    print("\nDICCIONARIO")

    for ingles in diccionario:
        print(f'{ingles}: {diccionario[ingles]}')

def consulta_palabra(diccionario):
    pal = input("\nIngrese la palabra en ingles a consultar: ")

    if pal in diccionario:
        print("En castellano significa:", diccionario[pal])

diccionario = main()
imprimir(diccionario)
consulta_palabra(diccionario)
