# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = j = 0
numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os números {numeros}')
# Para contar quantas vezes o número 9 apareceu.
n = numeros.count(9)
if n == 0:
    print('O número 9 não apareceu nenhuma vez. ')
else:
    print(f'O número 9 apareceu {n} vez(es).')
# Em que posição foi digitado o primeiro valor 3.
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}.')
else:
    print(f'O número 3 não apareceu em nenhuma posição.')
# Quais foram os números pares.
print('Os números pares: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
