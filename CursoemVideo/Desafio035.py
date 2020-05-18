# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

t1 = int(input('Digite o valor da primeira reta: '))
t2 = int(input('Digite o valor da segunda reta: '))
t3 = int(input('Digite o valor da terceira reta: '))

if t1 + t2 <= t3 and t2 + t3 <= t1 and t1 + t3 <=t2: #A soma de dois lados (mesmo sem saber quem é o maior ou m.) tem que ser maior do que o terceiro lado.
    print('Não é possível criar um triângulo com esses valores.')
else:
    print('É possível criar um triângulo com esses valores. ')

'''if t1 < t2 < t3 or t2 < t1 < t3:
    if t1 + t2 <= t3 and t2 + t1 <= t3:
        print('Não é possível criar um triângulo com esses valores. ')
    else:
        print('É possível criar um triângulo com esses valores. ')
if t3 < t1 < t2 or t1 < t3 < t2:
    if t3 + t1 <= t2 and t1 + t3 <= t2:
        print('Não é possível criar um triângulo com esses valores. ')
    else:
        print('É possível criar um triângulo com esses valores. ')
if t3 < t2 < t1 or t2 < t3 < t1:
    if t3 + t2 <= t1 and t2 + t3 <= t1:
        print('Não é possível criar um triângulo com esses valores. ')
    else:
        print('É possível criar um triângulo com esses valores. ')'''
