# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao
# final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
numeros.sort()
pares.sort()
impares.sort()
print(f'LISTA COMPLETA: {numeros} \nPARES:  {pares} \nIMPARES: {impares}')
