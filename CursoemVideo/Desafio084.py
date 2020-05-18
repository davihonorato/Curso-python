# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')  # conta a qtd de listas dentro da lista pessoas: a qtd de pessoas cadastradas.
print(f'O maior peso foi {maior}kg. Foi o peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor}kg. Foi o peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
