'''
  Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias 
  mensuales de dichos paises.
  Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
  Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.

  a) Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.

  b) Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.

  c) Calcular la temperatura media trimestral de cada país.

  d) Imprimir los nombres de los paises y las temperaturas medias trimestrales.

  e) Imprimir el nombre del pais con la temperatura media trimestral mayor.  
'''

paises = []
temperaturas = []
t_medias = []

cuantos_paises = 3

for i in range(cuantos_paises):
    print(f'Registro [{i + 1}]: ')
    nombre = input(f'País: ')
    t1 = int(input(f'Ta 1: '))
    t2 = int(input(f'Ta 2: '))
    t3 = int(input(f'Ta 3: '))

    paises.append(nombre)
    temperaturas.append([t1, t2, t3])

    t_media = (t1 + t2 + t3) / 3
    t_medias.append(t_media)


print(f'\n--- TEMPERATURAS ---')
for i in range(cuantos_paises):
    print(
        f'{paises[i]} --> {temperaturas[i][0]}°C | {temperaturas[i][1]}°C | {temperaturas[i][2]}°C --> Media: {t_medias[i]:.2f}°C')
