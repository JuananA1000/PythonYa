'''
  Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en 
  orden alfabético. 
'''

lista = []

for i in range(5):
    nombre = input(f'Nombre [{i+1}]: ')
    lista.append(nombre)

menor = lista[0]
for i in range(1, 5):
    if lista[i] < menor:
        menor = lista[i]

print(
    f'\nDe esta lista: {lista}, el de menor orden alfabético es: {menor}')
