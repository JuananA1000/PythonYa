'''
  Crear y cargar dos listas con los productos de 5 productos en una y sus respectivos precios en otra. Definir dos listas 
  paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado. 
'''

productos = []
precios = []

for i in range(5):
    print(f'Producto [{i+1}]: ')
    art = input('Artículo: ')
    pre = float(input('Precio: '))

    productos.append(art)
    precios.append(pre)

print('\nLos artículos mas caros que el primero son:')
for i in range(5):
    if precios[i] >= precios[1]:
        print(f'{productos[i]}, que cuesta {precios[i]}€\n')
