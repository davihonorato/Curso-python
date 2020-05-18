# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: MIRIM; até 14 anos: INFANTIL; até 19 anos: JUNIOR: até 20 anos: SÊNIOR; acima: MASTER

ano = int(input('Digite o ano do seu nascimento: '))
idade = 2020 - ano
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <=14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
