# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} números')
print(f'Os números digitados em ordem crescente: {valores}')
for pos, x in enumerate(valores):
    if x == 5:
        print(f'O valor 5 está na {pos+1}ª posição')
        break
    elif 5 not in valores:
        print('O valor 5 não foi digitado.')
        break
