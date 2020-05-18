# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
for c in range(0, 6, 1):
    n = int(input('Digite um número inteiro: '))
    s += n  # s = s + n
print(f'A SOMA DE TODOS OS NÚMEROS INTEIROS DIGITADOS É {s}')