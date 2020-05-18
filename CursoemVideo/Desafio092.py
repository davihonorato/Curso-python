# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
# idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
carteira = dict()
carteira['Nome'] = str(input('NOME: '))
nascimento = int(input('ANO DE NASCIMENTO: '))
carteira['Idade'] = datetime.now().year - nascimento
carteira['ctps'] = int(input('CARTEIRA DE TRABALHO (0 SE NÃO TIVER): '))
if carteira['ctps'] != 0:
    carteira['Ano de contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    carteira['Salário'] = float(input('Salário: R$ '))
    carteira['Aposentadoria'] = ((carteira['Ano de contratação'] + 60) - datetime.now().year) + carteira['Idade']
print('-'*30)
for k, v in carteira.items():
    print(f'{k}: {v}')
