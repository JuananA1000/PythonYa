'''
  Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más 
  caracteres. 
'''

lista = ['Juan Antonio', 'Tamara', 'Mario', 'Ana', 'Paco']
cuantos_nombres = 0

i = 0
while i < len(lista):
    if len(lista[i]) >= 5:
        cuantos_nombres += 1
    i += 1

print(f'Hay {cuantos_nombres} nombres de 5 o más caracteres.')
