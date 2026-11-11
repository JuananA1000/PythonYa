'''
  Cargar una cadena por teclado luego:
  a) Imprimir los dos primeros caracteres.
  
  b) Imprimir los dos últimos
  
  c) Imprimir todos menos el primero y el último caracter. 
'''

def cargar_cadena():
    return input('Ingrese una cadena: ')

def dos_primeros_caracteres(cadena):
    print(cadena[:2])

def dos_ultimos_caracteres(cadena):
    print(cadena[-2:])

def todo_menos_el_primero_y_el_ultimo(cadena):
    print(cadena[1:-1])

def main():
    cadena = cargar_cadena()
    print(f'\nCadena original: {cadena}')

    print('Los dos primeros caracteres son: ', end=' ')
    dos_primeros_caracteres(cadena)

    print('Los dos últimos caracteres son: ', end=' ')
    dos_ultimos_caracteres(cadena)
    
    print('Todos menos el primero y el último son: ', end=' ')
    todo_menos_el_primero_y_el_ultimo(cadena)

main()  