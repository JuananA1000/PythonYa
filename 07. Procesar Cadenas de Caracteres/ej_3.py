'''
  Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".
'''

mail = 'xxxxxx@gmail.com'
cuenta_arrobas = 0

i = 1
while i < len(mail):
    if mail[i] == '@':
        cuenta_arrobas += 1
    i += 1

if cuenta_arrobas > 1:
    print('Tiene MÁS de un @')
else:
    print('Tiene SOLO un @')
