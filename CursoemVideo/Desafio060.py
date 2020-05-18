#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

f = int(input('Digite um número: '))
fatorial = 1

if 1 >= f >= 0:
    print(f'1')
elif f < 0:
    print(f'O fatorial de número negativo não existe.')
else:
    print(f'{f}! = ', end='')
    while f >= 1:
        print(f, end='')
        print(' x ' if f > 1 else ' = ', end='')
        fatorial *= f
        f -= 1
print(fatorial)
