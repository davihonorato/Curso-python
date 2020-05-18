# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')

'''if v1 < v2 < v3:
    print(f'MAIOR: {v3} \nMENOR: {v1}')
elif v2 < v1 < v3:
    print(f'MAIOR: {v3} \nMENOR: {v2}')
elif v3 < v1 < v2:
    print(f'MAIOR: {v2} \nMENOR: {v3}')
elif v1 < v3 < v2:
    print(f'MAIOR: {v2} \nMENOR: {v1}')
elif v3 < v2 < v1:
    print(f'MAIOR: {v1} \nMENOR: {v3}')
else:
    print(f'MAIOR: {v2} \nMENOR: {v1}')'''
