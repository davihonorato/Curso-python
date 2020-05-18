# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço  da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 para viagens mais longas.

d = int(input('Distância da viagem (em Km): '))

if d <= 200:
    p = d*0.5
    print(f'Preço da passagem: {p}')
else:
    p = d*0.45
    print(f'Preço da passagem: {p}')
print('Tenha um bom dia.')

