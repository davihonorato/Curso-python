# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 89km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Insira a velocidade atual: '))
if vel > 89:
    multa = (vel-89)*7
    print(f'Você foi multado por excesso de velocidade num valor de R${multa},00.')

