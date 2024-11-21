'''
  Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe 
  retornar. La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.
'''

def main():

    dia = int(input('\nDía: '))
    mes = int(input('Mes: '))
    anno = int(input('Año: '))

    fecha = (dia, mes, anno)

    print(f'\nLa fecha introducida es: {fecha} ')

main()
