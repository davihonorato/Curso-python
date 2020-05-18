# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
turma = list()
while True:
    aluno['Nome'] = str(input('NOME: ')).upper()
    aluno['Media'] = float(input('MEDIA: '))
    if aluno['Media'] >= 7:
        aluno['Situação'] = 'APROVADO'
    else:
        aluno['Situação'] = 'REPROVADO'
    turma.append(aluno.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('\033[32m-\033[m'*20)
for c in turma:
    for k, al in c.items():
        print(f'{k}: {al}')
    print('-'*20)
