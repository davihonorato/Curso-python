# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

ni = int(input('Digite um número inteiro: '))
c = 1
soma = primeiro = 1
segundo = 0

print(segundo, primeiro, end=' ') # Para mostrar o primeiro número da sequência de Fibonacci
while c <= ni-1:  # É feita uma subtração porque vai sempre mostrar o primeiro número de Fibonacci com o 'if' acima
    print(f'{soma}', end=' ')
    segundo = primeiro
    primeiro = soma
    soma = primeiro + segundo
    c += 1
print('\nfim')

