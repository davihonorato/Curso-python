# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1240,00, calcule um aumento
# de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
if salario <= 1240.0:
    aumento = salario*0.15
    novo = salario + aumento
    print(f'NOVO SALÁRIO: {novo}')
else:
    aumento = salario*0.10
    novo = salario + aumento
    print(f'NOVO SALÁRIO: {novo}')
