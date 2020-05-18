# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

c = soma = 0  # 'c' para contar quantos números e 'soma' para somar todos os números.
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Você digitou {c} números e a soma deles é {soma}')
