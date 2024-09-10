'''
  Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar
  impuestos.
'''

sueldo = int(input('Ingresa tu sueldo: '))

if sueldo > 3000:
    print('Cobras ', sueldo, ' A PAGAR')
elif sueldo <= 3000:
    print('Cobras ', sueldo, ' no pagas')
