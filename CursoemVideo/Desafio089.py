# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.

dados = list()
boletim = list()
while True:
    dados.append(str(input('NOME: ')).upper().strip())
    dados.append(float(input('NOTA 1: ')))
    dados.append(float(input('NOTA 2: ')))
    boletim.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{"NOME":<18}{"MEDIA":<10}')
for c in boletim:
    for j in c:
        if j == 0:
            print(f'{j:>20}', end='')
        else:
            print(f'{j:>10}', end='')
    print()