# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoatual = date.today().year
maioridade = 0
menores = 0
for c in range(1, 8, 1):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = 2020 - anoatual
    if idade >= 18:
        maioridade += 1
    else:
        menores += 1
print(f'Quantidade de pessoas que ainda não atingiram a maioridade: {menores}')
print(f'Quantidade de pessoas que atingiram a maioridade: {maioridade}')