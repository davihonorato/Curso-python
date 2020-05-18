# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

n = int(input('Digite um valor: R$'))
print(f'Para o número {n}, nós podemos ter os seguintes valores: ')
print(f'AUMENTANDO 10% DE {n}: {moeda.aumentar(n)}')
print(f'DIMINUINDO 10% DE {n}: {moeda.diminuir(n)}')
print(f'O DOBRO DE {n} é: {moeda.dobro(n)}')
print(f'A METADE DE {n} é: {moeda.metade(n)}')
