'''
  Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
  Implementar las funciones:

  a) Carga de empleados.
  
  b) Impresión de los empleados y sus sueldos.
  
  c) Nombre del empleado con sueldo mayor.
  
  d) Cantidad de empleados con sueldo menor a 1000. 
'''

def el_mayor(li):
    mayor = li[0]
    for i in li:
        if i > mayor:
            mayor = i
    return mayor

def main():
    lista = []
    for i in range(2):
        print(f'\n-- EMPLEADO {i + 1} --')
        nombre = input('Nombre: ')
        sueldo = int(input('Sueldo: '))
        lista.append((nombre, sueldo))

    print("\nLista completa: ", lista)
    print("El empleado con sueldo mayor es: ", el_mayor(lista))

main()
