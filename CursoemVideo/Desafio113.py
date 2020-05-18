def leiaInt(txt):
    num = 0
    while True:
        n = str(input(txt))
        try:
            num = int(n)
        except:
            print('\033[0;31mDIGITE UM NÚMERO INTEIRO VÁLIDO. \033[m')
        else:
            return num


def leiaFloat(msg):
    num = 0
    while True:
        n = str(input(msg)).replace(',', '.')
        try:
            num = float(n)
        except:
            print('\033[0;31mDIGITE UM NÚMERO REAL VÁLIDO. \033[m')
        else:
            return num

txt = leiaInt('DIGITE UM NÚMERO INTEIRO: ')
msg = leiaFloat('DIGITE UM NÚMERO REAL: ')
print(f'Você digitou o número inteiro {txt} e o real {msg}')
