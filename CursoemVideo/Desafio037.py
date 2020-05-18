# Escreva um programa que eleia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário; 2 para octal; 3 para hexadecimal; (modulos)

ni = int(input('Digite um número inteiro: '))
c = int(input('Escolha a base que você quer converter: \n[1] BINÁRIO \n[2] OCTAL \n[3] HEXADECIMAL \n'))

if c == 1:
    print(f'O número \033[33m{ni}\033[m em binário é \033[33m{bin(ni)[2:]}\033[m')
elif c == 2:
    print(f'O número \033[33m{ni}\033[m em octal é \033[33m{oct(n1)[2:]}\033[m')
elif c == 3:
    print(f'O número \033[33m{ni}\033[m em hexadecimal é \033[33m{hex(ni)[2:]}\033[m')
else:
    print('\033[31mOPÇÃO INVÁLIDA! ')