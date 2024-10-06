'''
  Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero,
  febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.
  
  Ejemplo: dia: 10 mes: 2 año: 2018 
'''

dia = int(input('Ingresa un número de día: '))
mes = int(input('Ingresa un número de mes: '))
año = int(input('Ingresa un número de año: '))

# Intervalo dia: (ထ, 1)[1, 30](31, ထ)
# Intervalo mes: (ထ, 1)[1, 12](13, ထ)

if dia >= 1 and dia <= 31:
    if (mes >= 1) and (mes <= 3):
        print('La fecha %d/%d/%d corresponde al primer trimestre' %
              (dia, mes, año))
    elif (mes >= 4) and (mes <= 12):
        print('La fecha %d/%d/%d NO corresponde al primer trimestre' %
              (dia, mes, año))
    else:
        print('Fecha incorrecta')
else:
    print('Fecha incorrecta')
