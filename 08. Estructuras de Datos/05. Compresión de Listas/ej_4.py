'''
  Se tiene una lista de nombres de personas. Generar otra lista cuyos elementos sean a su vez listas con dos nombres 
  cada uno.
  Tener en cuenta que nunca se debe combinar el mismo nombre dos veces.
'''

nombres = ['juan', 'pablo', 'luis', 'mauro', 'hector']
nombres_compuestos = [[nombre1, nombre2] for nombre1 in nombres for nombre2 in nombres if nombre1 != nombre2]

print(nombres_compuestos)
