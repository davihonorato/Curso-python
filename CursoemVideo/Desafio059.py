# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números
# [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

operação = 0
while operação != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    operação = int(input('Que operação você quer realizar? \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa \n'))
    if operação == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif operação == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif operação == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
    elif operação == 4:
        pass
    else:
        if operação != 5:
            print('Opção inválida, digite novamente.')
        else:
            pass
print('fim')
