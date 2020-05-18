# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (US$1,00 = R$4,05)

di = float(input('Quando dinheiro vocÊ tem? R$'))
vdo = 4.05
do = di/vdo

print(f'Você pode comprar U${do:.2f}')