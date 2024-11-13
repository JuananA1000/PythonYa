'''
  Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe 
  mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.
'''

def calcular_sueldo(n_operario, pago_hora, horas_trabajadas):
    sueldo = pago_hora * horas_trabajadas

    print(f'{n_operario}, ha trabajado {horas_trabajadas} horas en el día y ha cobrado {sueldo}€')

def main():
    calcular_sueldo('Juan', 10, 8)
    calcular_sueldo(horas_trabajadas=8, n_operario='Paco', pago_hora=20)
    calcular_sueldo(pago_hora=12, horas_trabajadas=8, n_operario='Susana')

main()
