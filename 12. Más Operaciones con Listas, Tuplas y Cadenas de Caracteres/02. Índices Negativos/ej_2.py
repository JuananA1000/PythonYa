'''
   Cargar una cadena de caracteres por teclado. Mostrar la cadena al revés utilizando subíndices 
   negativos. 
'''

def al_reves(cadena):
    for x in range(-1, -len(cadena)-1, -1):
        print(cadena[x], end='')

def main():
    cadena = input("Ingrese una cadena: ")
    al_reves(cadena)

main()   