# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

maior = homens = mulheres = 0
while True:
    sexo = continuar = ' '
    print('-=-'*11)
    print(' - - - CADASTRE UMA PESSOA - - - ')
    print('-=-' * 11)
    idade = int(input('Idade? '))
    while sexo not in 'FM':
        sexo = str(input('Sexo? [F/M] ')).upper().strip()[0]
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'PESSOAS MAIORES DE IDADE: {maior}')
print(f'QUANTIDADE DE HOMENS: {homens}')
print(f'QUANTIDADE DE MULHERES MENORES DE 20 ANOS: {mulheres}')