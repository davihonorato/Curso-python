def leiaDinheiro(txt):
    ok = False
    while ok is False:
        n = input(txt).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO! "{n}" INVÁLIDO.\033[m')
        else:
            ok = True
            return float(n)


def leiaInt(msg):
    ok = False
    num = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if ok:
            break
    return num