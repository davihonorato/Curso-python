# Escreva um programa para aprova o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
print('\033[33m-=-'*10)
print('\033[36m - - EMPRÉSTIMO BANCÁRIO - -')
print('\033[33m-=-'*10)

casa = float(input('\033[34mQual o valor da casa que você irá comrar? '))
salario = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você predente pagar? '))
print('\033[33m-=-'*15)
print('\033[34mProcessando... ')
sleep(1)

tp = tempo*12  # Para saber quantos meses serão necessários para pagar a dívida.
porcentagem = salario*0.30  # 30% do salário
prestação = casa/tp  # Valor da prestação por mês

if prestação <= porcentagem:
    print('\033[36mVocê está habilitado para fazer o empréstimo.')
else:
    print('\033[31mVocê não está habilitado para fazer o empréstimo.')
print('\033[32mTenha um ótimo dia.')