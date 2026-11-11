'''
  Implementación de una función recursiva.
'''

def repetir():
    print("Hola, mundo!")
    repetir()
    
repetir() # Este código generará un error de Recursión Infinita => RecursionError: maximum recursion depth exceeded
