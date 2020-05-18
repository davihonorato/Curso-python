# Faça um algorítimo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.

s = float(input('Digite o seu salário: '))
a = s*0.15
sn = s+a
print(f'Seu novo salário (com aumento de 15%): R${sn:.2f}')