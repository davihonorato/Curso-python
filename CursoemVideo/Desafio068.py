# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
soma = 0  # Soma dos números jogados pelo computer e pelo player
vitorias = 0  # Vitórias consecutivas do player
while True:
    print('-=-' * 20)
    player = str(input('PAR OU ÍMPAR? [P/I]')).upper().strip()[0]
    valor_player = int(input('Digite um valor: '))
    valor_computer = randint(0, 10)
    soma = valor_player + valor_computer
    print(f'Você escolheu {valor_player} e o computer escolheu {valor_computer}, ', end='')
    print('deu par!' if soma % 2 == 0 else 'deu ímpar!')
    if soma % 2 == 0:
        soma = 'P'
    else:
        soma = 'I'
    if soma == player:
        vitorias += 1
        print('\033[32mVocê venceu!\033[m')
    else:
        print('\033[31mVocê perdeu!\033[m ')
        break
print('-=-' * 20)
print(f'Você ganhou {vitorias} vez(es)')
