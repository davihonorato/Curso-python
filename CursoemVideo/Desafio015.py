# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a se pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

dias = int(input('Por quantos dias ele foi alugado? '))
dp = float(input('Quantos km foram percorridos? '))
total = (dias*60)+ (dp*0.15)

print(f'O valor total a se pagar é de R${total:.2f}')