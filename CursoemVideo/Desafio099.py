# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    c = maior = 0  #contador e o maior
    print('--'*15)
    print('ANALISANDO OS VALORES...')
    for v in num:
        sleep(0.5)
        print(v, end=' ')
        if c == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        c += 1
    sleep(1)
    print(f'\nFORAM ANALISADOS {c} VALORES E O MAIOR DELES É {maior}')


maior(5, 8, 3, 6, 10)
maior(4, 6, 9, 1)
maior(11, 3, 1)
maior(2, 0)
maior(0)
