# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
termo = a1  #Uma variável para se atualizar.
an = a1 + (10 - 1)*r
while c <= 10:
    print(f'{termo}', end='')
    print(f' -> ' if c !=10 else '', end='')
    termo += r
    c += 1
print('\nfim')
