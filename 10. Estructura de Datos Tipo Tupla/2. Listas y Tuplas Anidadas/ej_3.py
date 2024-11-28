'''
  Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
  En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con 
  componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.

  a) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.

  b) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias. 
  
  Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:

  candidatos=[('juan', [('cordoba', 100), ('buenos aires', 200)]), ('ana', [('cordoba', 55)]), ('luis', [('buenos aires', 20)]) ]
'''

def imprimir_votos_totales(candidatos):
    resultados = []

    for candidato, provincias in candidatos:
        total_votos = sum(votos for _, votos in provincias)
        resultados.append((candidato, total_votos))
        
    return resultados

def main():
    candidatos = []
    cuantos_candidatos = 2
    cuantas_prov = 3

    for i in range(cuantos_candidatos):
        print(f'\n--CANDIDATO {i+1}-- ')
        nombre_candidato = input(f'Nombre: ')
        votos_por_prov = []

        for j in range(cuantas_prov):
            nombre_provincia = input(f'Provincia {j+1}: ')
            votos = int(input(f'Nº de votos en {nombre_provincia}: '))

            votos_por_prov.append((nombre_provincia, votos))

        candidatos.append((nombre_candidato, votos_por_prov))

    votos_totales = imprimir_votos_totales(candidatos)

    print(f'\nLista de candidatos: {candidatos}')

    print(f'\nVotos por candidato:')
    for candidato, total_votos in votos_totales:
        print(f'Candidato: {candidato} | Votos: {total_votos}')

main()