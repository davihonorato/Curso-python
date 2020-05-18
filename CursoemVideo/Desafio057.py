# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0
while sexo != 1:
    s = str(input('Digite o seu sexo: ')).upper()
    if s == 'F' or s == 'M':
        sexo = 1
    else:
        print('\033[31mINFORMAÇÃO INCORRETA.\033[m')
print('Você é do sexo {}'.format(s))
