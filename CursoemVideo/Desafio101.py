# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        voto = f'COM {idade} ANOS: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        voto = f'COM {idade} ANOS: VOTO OPCIONAL'
    elif 18 <= idade < 65:
        voto = f'COM {idade} ANOS: VOTO OBRIGATÓRIO'
    return voto

ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))
