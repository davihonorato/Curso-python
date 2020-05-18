# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

qtd = soma = pessoa = 0
while pessoa != 999:
    soma += pessoa
    qtd += 1
    pessoa = int(input('Digite um número inteiro: '))
print(f'Você digitou {qtd} números')
print(f'A soma dos números que você digitou é {soma}')