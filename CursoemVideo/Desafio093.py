# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gols = list()
jogador['NOME'] = str(input('Nome do Jogador: ')).upper().strip()
partidas = int(input('Quantidade de partidas: '))
if partidas != 0:
    for c in range(0, partidas):
        gols.append(int(input(f'Quantidade de gols na partida {c+1}: ')))
else:
    gols.append(0)
jogador['GOLS'] = gols[:]
jogador['TOTAL'] = sum(gols)
print('-=-'*20)
print(jogador)
print('-=-'*20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=-'*20)
print(f'O jogador {jogador["NOME"]} jogou {partidas} partidas: ')
for c in range(0, partidas):
    print(f'Na partida {c+1}, ele marcou {gols[c]} gol(s).')
print(f'Num total de {jogador["TOTAL"]} gols.')
