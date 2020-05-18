# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
player = 11  # Para que o programa possa rodar sem problemas.
c = 0  # Contador
computer = randint(0, 10)
while player != computer:
    if c == 0:
        print('\033[34mVOU PENSAR EM UM NÚMERO. TENTE ADINHAR!')
        player = int(input('Qual é o seu palpite? \033[m'))
    else:
        player = int(input('\033[31mVOCÊ ERROU! TENTE NOVAMENTE: \033[31m'))
    c += 1
if c <= 3:
    print(f'\033[34mVOCÊ ACERTOU, PARABENS! \nQUANTIDADE DE TENTATIVAS: \033[33m{c}')
else:
    print(f'\033[34mFINALMENTE VOCÊ ACERTOU, HEIN!? \nQUANTIDADE DE TENTATIVAS: \033[33m{c}')
