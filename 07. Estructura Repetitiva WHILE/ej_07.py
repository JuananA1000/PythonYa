'''
  En una empresa trabajan n empleados cuyos sueldos oscilan entre 1100€ y 1500€, realizar un programa que lea los 
  sueldos que cobra cada empleado e informe cuántos empleados cobran entre 1100€ y 1300€ y cuántos cobran más de 1300€. 
  Además el programa deberá informar el importe que gasta la empresa en sueldos al personal. 
'''

empleados = int(input('Nº Empleados: '))
importe_total = 0
cont1 = 0
cont2 = 0

i = 1
while i <= empleados:
    sueldo = int(input('Sueldo [%d]: ' % i))

    if sueldo >= 1100 and sueldo <= 1300:
        cont1 += 1
    elif sueldo > 1300:
        cont2 += 1

    importe_total += sueldo
    i += 1

print('Empleados entre 1100€ y 1300€: ', cont1)
print('Empleadosde más de 1300€: ', cont2)
print(f'Importe total de la empreS.A.: {importe_total:.2f}€')
