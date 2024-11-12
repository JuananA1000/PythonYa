'''
  Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
  Definir las siguientes funciones: 

  a) Cargar los nombres de articulos y sus precios.
  
  b) Imprimir los nombres y precios.
  
  c) Imprimir el nombre de artículo con un precio mayor
  
  d) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
'''

def return_li(li_nom, li_pre):
    return li_nom, li_pre

def return_el_mas_caro(li_nom, li_pre):
    max_index = li_pre.index(max(li_pre))
   
    return li_nom[max_index]

def mostrar_articulos_por_precio(li_nom, li_pre):
    importe = float(input('Ingrese el importe máximo: '))
    articulos_filtrados = []

    for i in range(len(li_pre)):
        if li_pre[i] <= importe:
            articulos_filtrados.append((li_nom[i], li_pre[i]))

    return articulos_filtrados

def main():
    nombres = []
    precios = []
    cuantos_articulos = 5

    for i in range(cuantos_articulos):
        print(f'\nProducto {i + 1}')
        nombre = input('Nombre: ')
        precio = float(input('Precio: '))

        nombres.append(nombre)
        precios.append(precio)

    res_nombres,  res_precios = return_li(nombres, precios)
    mas_caro = return_el_mas_caro(nombres, precios)
    articulos_filtrados = mostrar_articulos_por_precio(nombres, precios)
    
    print('\nPRECIOS POR ARTÍCULO')
    for i in range(cuantos_articulos):
        print(f'Nombre: {res_nombres[i]} | Precio: {res_precios[i]}')

    print(f'\nArtículo MÁS CARO: {mas_caro}')

    print(f'\nArtículos con precio menor o igual al importe ingresado: {articulos_filtrados}')

main()
