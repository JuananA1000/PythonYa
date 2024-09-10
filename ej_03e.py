'''
   Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.
'''
horas_trabajadas = int(input('Horas trabajadas: '))
valor_por_hora = float(input('Valor por hora: '))

sueldo_mensual = (valor_por_hora * horas_trabajadas) * 30

print('Mi sueldo mensual: ', sueldo_mensual, '€')
