# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi
# o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'  # O usuário uniciou o programa.
media = soma= maior = menor = c = 0

while resp == 'S':
    c += 1
    n = int(input('Digite um número inteiro: '))
    if n >= maior:
        maior = n
        if c == 1:
            menor = maior
    elif n < menor:
        menor = n
    soma += n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/c
print(f'Você digitou {c} números')
print(f'O MAIOR VALOR: {maior} \nO MENOR VALOR: {menor} \nA MÉDIA: {media}')