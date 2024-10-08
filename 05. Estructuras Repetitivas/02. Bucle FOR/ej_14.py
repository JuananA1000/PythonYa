'''
  Se cuenta con la siguiente información:
  Las edades de 5 estudiantes del turno mañana.
  Las edades de 6 estudiantes del turno tarde.
  Las edades de 11 estudiantes del turno noche.
  Las edades de cada estudiante deben ingresarse por teclado.
  
  a) Obtener el promedio de las edades de cada turno (tres promedios)

  b) Imprimir dichos promedios (promedio de cada turno)
  
  c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor. 
'''

suma_mañana = 0
suma_tarde = 0
suma_noche = 0

print("\nIngrese las edades de los 5 estudiantes del turno mañana:")
for i in range(5):
    edad = int(input(f"Estudiante {i+1}: "))
    suma_mañana += edad

promedio_mañana = suma_mañana / 5

print("\nIngrese las edades de los 6 estudiantes del turno tarde:")
for i in range(6):
    edad = int(input(f"Estudiante {i+1}: "))
    suma_tarde += edad

promedio_tarde = suma_tarde / 6

print("\nIngrese las edades de los 11 estudiantes del turno noche:")
for i in range(11):
    edad = int(input(f"Estudiante {i+1}: "))
    suma_noche += edad

promedio_noche = suma_noche / 11

print(f"\nPromedio de edades del turno mañana: {promedio_mañana}")
print(f"Promedio de edades del turno tarde: {promedio_tarde}")
print(f"Promedio de edades del turno noche: {promedio_noche}")

if promedio_mañana > promedio_tarde and promedio_mañana > promedio_noche:
    print("El turno mañana tiene el mayor promedio de edades.")
elif promedio_tarde > promedio_mañana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene el mayor promedio de edades.")
else:
    print("El turno noche tiene el mayor promedio de edades.")
