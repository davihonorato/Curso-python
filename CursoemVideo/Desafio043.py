# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status , de acordo com a tabela abaixo;
# abaixo de 18.5: ABAIXO DO PESO; entre 18.5 e 25: PESO IDEAL; 25 até 30: SOBREPESO; 30 até 40: OBESIDADE; acima de 40: OBESIDADE MÓRBIDA;

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/altura**2

if imc < 18.5:
    print('ABAIXO DO PESO')
    print(f'IMC: {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
    print(f'IMC: {imc:.2f}')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
    print(f'IMC: {imc:.2f}')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
    print(f'IMC: {imc:.2f}')
else:
    print('OBESIDADE MÓRBIDA')
    print(f'IMC: {imc:.2f}')