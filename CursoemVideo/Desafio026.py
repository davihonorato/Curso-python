#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra "A": {frase.count("A")}')
print(f'Posição do primeiro "A": {frase.find("A")+1}')
print(f'Posição do último "A": {frase.rfind("A")+1}')

# Você pode expandir essa ideia dizendo a colocação do primeiro "A" e do ultimo "A" em relação a apenas letras.