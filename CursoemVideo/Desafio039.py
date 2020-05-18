# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar; Se já passou do tempo do alistamento. Seu programa trambém deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano do seu nascimento: '))
idade = 2020 - ano

if idade < 18:
    print(f'Ainda falta {18 - idade} anos para se alistar ao serviço militar! ')
elif idade > 18:
    print(f'Você passou {(18 - idade)*(-1)} do tempo de se alistar ao serviço militar! ')
else:
    print(f'Está no momento de se alistar ao serviço militar! ')
print('BRASIL ACIMA DE TUDO, DEUS ACIMA DE TODOS.')