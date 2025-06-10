'''
  Confeccionar una función que le enviemos un número de mes como parámetro y nos retorne una tupla con todos los nombres 
  de meses que faltan hasta fin de año.
'''

def meses_faltantes(numero_mes):
    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
             'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
    return meses[numero_mes:]

def main():
    numero_mes = int(input('Ingrese un número de mes: '))
    mesesfalta = meses_faltantes(numero_mes)

    print(f'Los meses que faltan son: {mesesfalta}')

main()
