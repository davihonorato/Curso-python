# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
g1 = str(input('ALUNO 1: '))
g2 = str(input('ALUNO 2: '))
g3 = str(input('ALUNO 3: '))
g4 = str(input('ALUNO 4: '))

grupos = [g1, g2, g3, g4]
shuffle(grupos)
print('A ordem de apresentação será:')
print(grupos)
