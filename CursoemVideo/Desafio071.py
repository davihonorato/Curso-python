# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues.OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor que será sacado: '))
total = valor
cedula = 50
qtd = 0
while True:
    if total >= cedula:
        total -= cedula
        qtd += 1
    else:
        if qtd > 0:
            print(f'Quantidade de notas de R${cedula}: {qtd}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        qtd = 0
        if total == 0:
            break
print('OBRIGADO PELA OPÇÃO. TENHA UM BOM DIA!')

# OUTRA FORMA:
'''valor = int(input('Digite o valor que será sacado: '))
nota_50 = valor // 50
resto1 = valor % 50
nota_20 = resto1 // 20
resto2 = resto1 % 20
nota_10 = resto2 // 10
resto3 = resto2 % 10
nota_1 = resto3
print(f'NOTAS DE 50: {nota_50}')
print(f'NOTAS DE 20: {nota_20}')
print(f'NOTAS DE 10: {nota_10}')
print(f'NOTAS DE 1: {nota_1}')'''
