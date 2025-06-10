'''
  Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
  Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del 
  país con mayor cantidad de habitantes.
'''

def return_el_mas_poblado(li_paises):
    mayor = li_paises[0]

    for i in range(1, len(li_paises)):
        if li_paises[i] > mayor:
            mayor = li_paises[i]
    return mayor

def main():
    paises = []

    for i in range(5):
        print(f'\nPaís [{i+1}]')
        nom = input('Nombre: ')
        hab = input('Habitantes: ')

        # Agregamos los datos en forma de TUPLA
        paises.append((nom, hab))
    
    max_poblacion = return_el_mas_poblado(paises)

    print(f'\nLista de países: {paises}')
    print(f'El país con mayor población es: {max_poblacion}')

main()
