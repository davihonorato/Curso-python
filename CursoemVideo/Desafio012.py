# Faça um algorítimo que leia o preço de um produto, calcule e mostre seu novo preço com 5% de desconto.

p = float(input('Preço do produto: '))
d = p*0.05
np = p-d

print(f'O preço com desconto de 5%: {np:.2f} ')