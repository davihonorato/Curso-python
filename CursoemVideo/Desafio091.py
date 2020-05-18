# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário
# em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
ranking = list()
jogadores = {
    'Jogador1': randint(0, 6),
    'Jogador2': randint(0, 6),
    'Jogador3': randint(0, 6),
    'Jogador4': randint(0, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
print('-=-'*10)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, j in enumerate(ranking):
    print(f'{c+1}º lugar: {j[0]} com {j[1]}')
