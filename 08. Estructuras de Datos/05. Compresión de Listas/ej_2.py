'''
  Se tiene una lista con un conjunto de tuplas con los nombres y edades de personas:
  Generar una lista con las personas mayores de edad.
'''

personas = [('pedro', 33), ('ana', 3), ('juan', 13), ('carla', 45)]
personas_mayores = [persona for persona in personas if persona[1] >= 18]

print(f"Personas mayores de edad: {personas_mayores}")
