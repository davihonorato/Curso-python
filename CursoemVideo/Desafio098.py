# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2 c) uma contagem personalizada
from time import sleep


def contador(y, x, z):
    if z == 0:
        z = 1
    elif z < 0:
        z *= -1
    print(f'A CONTAGEM DE {y} ATÉ {x} de {z} em {z}: ')
    if y < x:
        for c in range(y, x+1, z):
            sleep(0.5)
            print(c, end=' ')
    else:
        if z > 0:
            for c in range(y, x-1, -z):
                sleep(0.5)
                print(c, end=' ')
    print()
    print('--' * 15)


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('INÍNIO: ')), int(input('FIM:    ')), int(input('PASSO:  ')))


