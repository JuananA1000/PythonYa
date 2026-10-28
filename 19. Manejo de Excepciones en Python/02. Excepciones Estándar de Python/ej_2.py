'''
  Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número de mes y mostrar seguidamente el 
  nombre de dicho mes. Capturar la excepción IndexError.
'''

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    numero_mes = int(input("Ingrese el número del mes (1-12): "))
    nombre_mes = meses[numero_mes - 1]
    print(f"El mes {numero_mes} es: {nombre_mes}")
except IndexError:
    print("Error: Número de mes inválido. Debe estar entre 1 y 12.")
