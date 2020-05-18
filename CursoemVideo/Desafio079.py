# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
valores = []
while True:
    valor = int(input('Digite um número inteiro: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Erro: o valor adicionado já existe.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
valores.sort()
print('Ordem crescente: ', end='')
for i in valores:
    print(i, end=' ')
