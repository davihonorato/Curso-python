# Refaça o desafio009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número: '))
print(f'TABUADA DE {n}: ')
for c in range(0, 11, 1):
    print(f'{c} x {n} = {c*n} ')
print('FIM')
