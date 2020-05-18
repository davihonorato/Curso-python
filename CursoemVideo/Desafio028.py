# Escreva um programa que faça o computador "pensar" em um número inteiro etre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador o programa deverá escrever na tela se o usuário venceu ou não.

import random
num = random.randint(0, 5)

n = int(input('Acabei de pensar em um número de 0 a 5. Em que número eu pensei? '))
if n == num:
    print('PARABENS, VOCÊ ACERTOU! ')
else:
    print(f'NÃO FOI DESSA VEZ! PENSEI EM {num}')
print('Obrigado por participar. ^-^')

