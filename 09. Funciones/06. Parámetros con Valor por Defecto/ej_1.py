'''
  Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter. La 
  función debe mostrar el string subrayado con el caracter que indica el segundo parámetro
'''

def subrayar(titulo, caracter='*'):
    print(titulo)
    print(caracter * len(titulo))

def main():
    subrayar('Titulo')
    subrayar('Ventas', '-')

main()
