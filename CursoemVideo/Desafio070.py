# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.
total = qtd = c = 0  # o total de gastos na compra, a quantidade de produtos que custam mais de R$1000 e o contador
barato = ''  # produto mais barato
menor = 0  # analisar o preço do produto
while True:
    nome = str(input('Qual é o produto? ')).upper().strip()
    preço = float(input('Qual é o preço? '))
    c += 1
    total += preço
    if preço > 1000:
        qtd += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = nome
    cont = ' '  # Para poder iniciar o programa a seguir
    while cont not in 'SN':  # Enquanto o usuário não digitar 'S' ou 'N', o programa continuará perguntando.
        cont = str(input('Você quer adcionar mais um produto? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'TOTAL DOS GASTOS NA COMPRA: {total:.2f}')
print(f'QUANTIDADE DE PRODUTOS QUE CUSTAM MAIS DE R$1000: {qtd}')
print(f'PRODUTO MAIS BARATO: {barato}')
