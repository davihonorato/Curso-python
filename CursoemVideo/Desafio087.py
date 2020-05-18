# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
somap = somat = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for j in range(0, 3):
        matriz[c][j] = int(input(f'Digite um valor para [{c}, {j}]: '))
        if matriz[c][j] % 2 == 0:
            somap += matriz[c][j]
        if c == 1 and j == 0:
            maior = matriz[c][j]
        else:
            if c == 1 and matriz[c][j] > maior:
                maior = matriz[c][j]
for c in range(0, 3):
    somat += matriz[c][2]
for c in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[c][n]:^3}]', end=' ')
    print()
print(f'A soma de todos os valores pares é {somap}')
print(f'A soma de todos os valoers da terceira coluna é {somat}')
print(f'O maior valor da segunda linha é {maior}')
