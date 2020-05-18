# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()  # ou apenas: []
maior = menor = 0
pos1 = pos2 = 0
for c in range(0, 5):
    valores.append(int(input('Digite um número inteiro: ')))
for pos, n in enumerate(valores):
    if pos == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
            pos1 = pos
        if n < menor:
            menor = n
            pos2 = pos
print(f'O maior número foi {maior}, na posição {pos1}')
print(f'O menor número foi {menor}, na posição {pos2}')
