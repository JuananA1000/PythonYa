'''
  Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona 
  con mayor altura.
'''

nom1 = input("Ingrese nombre 1: ")
edad1 = int(input("Ingrese la edad 1:"))
alt1 = float(input("Ingrese la altura 1:"))

nom2 = input("Ingrese nombre 1: ")
edad2 = int(input("Ingrese la edad 1: "))
alt2 = float(input("Ingrese la altura 1: "))

if alt1 > alt2:
    print("La persona mas alta es: ", nom1)
else:
    print("La persona mas alta es: ", nom2)
    
