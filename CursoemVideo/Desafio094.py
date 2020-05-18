# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoas = list()
dados = dict()
mulheres = list()
imedia = list()
idade = 0
while True:
    dados['NOME'] = str(input('Nome: ')).upper().strip()
    dados['SEXO'] = ' '
    while dados['SEXO'] not in 'FM':
        dados['SEXO'] = str(input('Sexo: ')).upper().strip()
    dados['IDADE'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    idade += dados['IDADE']
    media = idade // len(pessoas)
    if dados['SEXO'] == 'F':
        mulheres.append(dados.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-=-'*20)
print(f'[ A ] Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'[ B ] A media de idade é: {media} anos')
print(f'[ C ] Mulheres cadastradas: ', end='')
for c in mulheres:
    print(c['NOME'], end=' ')
print()
for p in pessoas:
    if p['IDADE'] > media:
        imedia.append(p.copy())
print(f'[ D ] Pessoas acima da media: ')
for i in imedia:
    for k, v in i.items():
        print(f'{k} = {v}', end='; ')
    print()
