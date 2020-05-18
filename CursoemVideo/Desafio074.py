# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
n = maior = menor = 0
num = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))  # gerando cinco números aleatórios entre 1 e 20
print('Os números sorteados foram: ', end='')
for c in num:
    print(f'{c}', end='')
    print(', ' if n < 4 else '. ', end='')

    '''if n == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c'''
    n = n+1
print(f'\nO menor número: {min(num)}')  # Propriedade que pode ser utilizada com as tuplas
print(f'O maior número: {max(num)}')

'''print(f'\nO menor número: {menor}')
print(f'O maior número: {maior}')'''