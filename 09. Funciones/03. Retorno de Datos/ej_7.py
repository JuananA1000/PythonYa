'''
  Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'. 
'''

def cuenta_aes(str):
    cuenta_aes_may = 0
    cuenta_aes_min = 0

    i = 0
    while i < len(str):
        if str[i] == 'A':
            cuenta_aes_may += 1

        if str[i] == 'a':
            cuenta_aes_min += 1
        i += 1

    return cuenta_aes_min, cuenta_aes_may

def main():
    frase = input('Introduce frase: ')

    n_min, n_may = cuenta_aes(frase)

    print(f'La frase "{frase}"\ntiene {n_min} aes minúsculas y {n_may} aes mayúsculas')

main()
