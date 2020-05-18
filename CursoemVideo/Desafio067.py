# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.

while True:
    print('-=-'*20)
    n = int(input('Você quer ver a tabuada de que número? '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n*c}')
print('fim')
