# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.
from random import randint
from time import sleep
palpites = []
jogos = list()
i = 1  # contador
qtd = int(input('Quantos jogos serão feitos? '))
for c in range(0, qtd):
    for j in range(0, 6):
        sort = randint(1, 60)
        if sort not in palpites:
            palpites.append(sort)
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
print('- - '*7)
print(f' - - SORTEANDO {qtd} JOGOS - - ')
print('- - '*7)
for c in jogos:
    sleep(1)
    print(f'{i}º JOGO: {c}')
    i += 1
print(F'{"- - - - BOA SORTE! - - - - ":^20}')
