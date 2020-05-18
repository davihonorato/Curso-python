def aumentar(x, aum, formato=False):
    valor = x + (x*(aum/100))
    return valor if not formato else moeda(valor)


def diminuir(x, red, formato=False):
    porc = x * (red/100)
    valor = x - porc
    return valor if formato is False else moeda(valor)


def dobro(x, formato=False):
    dobro = x * 2
    return dobro if not formato else moeda(dobro)


def metade(x, formato=False):
    met = x/2
    return met if formato is False else moeda(met)

def moeda(x, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')

def resumo(x, aum=0, red=0):
    print('---'*9)
    print('      RESUMO DO VALOR      ')
    print('---'*9)
    print(f'VALOR: \t\t\t{moeda(x)}')
    print(f'AUMENTO({aum}%): \t{aumentar(x, aum, True)}')
    print(f'REDUÇÃO({red}%): \t{diminuir(x, red, True)}')
    print(f'DOBRO: \t\t\t{dobro(x, True)}')
    print(f'METADE: \t\t{metade(x, True)}')
    print('---' * 9)
