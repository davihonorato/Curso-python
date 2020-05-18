# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

ni = int(input('Digite um número inteiro: '))
div = 0  # Para saber quantas vezes o número irá ser dividido
for c in range(1, ni+1):
    if ni % c == 0:
        print(f'\033[1;32m {c}', end=' ')
        div += 1
    else:
        print(f'\033[1;31m {c}', end=' ')
print(f'\n \033[34mO número {ni} foi dividido {div} vezes,', end=' ')
if div == 2:
    print('sendo assim, ele é primo.')
else:
    print('sendo assim, ele não é primo.')
