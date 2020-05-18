# Crie um porograma que faça o computador jogar Jokempô com você.
from emoji import emojize
from random import randint
import sys
from time import sleep

print('\033[33m-=-' * 7)
print('\033[36m - - - JOKEMPÔ - - - ')
print('\033[33m-=-' * 7)

print('\033[34mREGRAS: ')
print(emojize('1- PEDRA (:fist:)', use_aliases=True))
print(emojize('2- PAPEL (:newspaper:)', use_aliases=True))
print(emojize('3- TESOURA (:scissors:)', use_aliases=True))
print(emojize('0- SAIR (:runner:)', use_aliases=True))
print('\033[33m-=-' * 7)

computer = randint(1, 3)  # COMPUTADOR
jogador = int(input('\033[36mJOGADA: '))  # JOGADOR

if jogador == 0:  # O jogador sai do jogo.
    print('\033[36mENCERRANDO...')
    sleep(2)
    sys.exit()
elif jogador == computer:  # O jogador empata com o computador
    print('\033[36mPROCESSANDO...')
    sleep(2)
    print('\033[33m-=-' * 7)
    print('\033[35mEMPATE!')
    if computer == 1:
        computer = emojize(':fist:', use_aliases=True)
    elif computer == 2:
        computer = emojize(':newspaper:', use_aliases=True)
    elif computer == 3:
        computer = emojize(':scissors:', use_aliases=True)
    if jogador == 1:
        jogador = emojize(':fist:', use_aliases=True)
    elif jogador == 2:
        jogador = emojize(':newspaper:', use_aliases=True)
    elif jogador == 3:
        jogador = emojize(':scissors:', use_aliases=True)
    print(f'COMPUTADOR: {computer} \nVOCÊ: {jogador}')
elif 1 == jogador and 3 == computer or jogador == 2 and computer == 1 or jogador == 3 and computer == 2:  # O jogador ganha.
    print('\033[36mPROCESSANDO...')
    sleep(2)
    print('\033[1;33m-=-' * 7)
    print('\033[32mPARABÉNS, VOCÊ VENCEU!')
    if computer == 1:
        computer = emojize(':fist:', use_aliases=True)
    elif computer == 2:
        computer = emojize(':newspaper:', use_aliases=True)
    elif computer == 3:
        computer = emojize(':scissors:', use_aliases=True)
    if jogador == 1:
        jogador = emojize(':fist:', use_aliases=True)
    elif jogador == 2:
        jogador = emojize(':newspaper:', use_aliases=True)
    elif jogador == 3:
        jogador = emojize(':scissors:', use_aliases=True)
    print(f'COMPUTADOR: {computer} \nVOCÊ: {jogador}')
elif jogador == 3 and computer == 1 or jogador == 1 and computer == 2 or jogador == 2 and computer == 3:  # O jogador perde.
    print('\033[36mPROCESSANDO...')
    sleep(2)
    print('\033[33m-=-' * 7)
    print('\033[31mLOSER!! VOCÊ PERDEU, EU GANHEI!')
    if computer == 1:
        computer = emojize(':fist:', use_aliases=True)
    elif computer == 2:
        computer = emojize(':newspaper:', use_aliases=True)
    elif computer == 3:
        computer = emojize(':scissors:', use_aliases=True)
    if jogador == 1:
        jogador = emojize(':fist:', use_aliases=True)
    elif jogador == 2:
        jogador = emojize(':newspaper:', use_aliases=True)
    elif jogador == 3:
        jogador = emojize(':scissors:', use_aliases=True)
    print(f'COMPUTADOR: {computer} \nVOCÊ: {jogador}')
else:  # Opção inválida.
    print('\033[31mCOMANDO INVÁLIDO!')
