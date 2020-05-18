# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras no total (sem considerar os espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome: ')).strip()

print(f'maiusculas: {nome.upper()}')
print(f'minusculas: {nome.lower()}')
print(f'letras ao todo: {len(nome) - nome.count(" ")}')
print(f'letras no primeiro nome: {len(nome.split()[0])}') # print(f'letras no primeiro nome: {nome.find(" ")}'
