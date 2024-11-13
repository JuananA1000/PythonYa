'''
  Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. Definir un segundo 
  parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de 
  multiplicar como lo indica el segundo parámetro.
  Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados. 
'''

def tabla_del(valor, termino=10):

    print('\n')  # Esto es solo para poner un espacio entre tabla y tabla
    # for i in range(termino): Con este bucle hace que el segundo factor de 0 a 9
    for i in range(1, termino+1):
        print(f'{valor} x {i} = {valor * i}')

def main():
    tabla_del(5)
    tabla_del(6, termino=3)

main()
