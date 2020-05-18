# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('LÁPIS', 1.75,
            'BORRACHA', 2,
            'CADERNO', 20,
            'CANETAS', 7,
            'MOCHILA', 120)
print('-'*40)
print(f'{"PRODUTOS":^40}')
print('-'*40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='R$')
    else:
        print(f'{produtos[c]:>7.2f}')
print('-'*40)
