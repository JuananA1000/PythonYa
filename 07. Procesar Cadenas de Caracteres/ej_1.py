'''
  Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que 
  lo componen.
'''

nombre = 'Juanan'

'''
  Método 1: Index Operator

  Ventajas:
  - Fácil de implementar
  - Tiempo de ejecución rápido
  Desventajas:
  - Solo funciona con cadenas
  - No funciona con otros tipos de secuencias (como listas o tuplas)
'''
print('Index operator: ', nombre[0])


'''
  Método 2: Slicing

  Ventajas:
  - Funciona con cualquier tipo de secuencia (cadenas, listas, tuplas)
  - Se puede utilizar para extraer un subconjunto de elementos de una secuencia
  Desventajas:
  - Más complejo de implementar que el método 1
  - Tiempo de ejecución más lento en comparación con el método 1 y el método 2
'''
print('Slicing: ', nombre[:1])

print('Número de letras: ', len(nombre))
