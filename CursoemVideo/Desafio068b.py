# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo. --> while x not in 'ccc'
from random import randint
vitorias = 0
while True:
    print('-=-'*15)
    player = ' '
    while player not in 'PI':
        player = str(input('PAR OU IMPAR? [P/I] ')).upper().strip()[0]
    num_player = int(input('Qual a sua jogada? '))
    num_computer = randint(0, 10)
    soma = num_player + num_computer
    print(f'Você escolheu {num_player} e o computer escolheu {num_computer},', end=' ')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU IMPAR!')
    if player == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU! ')
            vitorias += 1
        else:
            print('VOCÊ PERDEU! ')
            break
    else:
        if soma % 2 != 0:
            print('VOCÊ GANHOU! ')
            vitorias += 1
        else:
            print('VOCÊ PERDEU! ')
            break
print('-=-'*15)
print(f'GAME OVER! Você ganhou {vitorias} vez(es).')
