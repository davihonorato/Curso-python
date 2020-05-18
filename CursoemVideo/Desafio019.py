# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude a ele, lendo o nome de todos
# e escrevendo o nome do escolhido. (módulos)

import random
a1 = str(input('ALUNO 1: '))
a2 = str(input('ALUNO 2: '))
a3 = str(input('ALUNO 3: '))
a4 = str(input('ALUNO 4: '))

alunos = [a1, a2, a3, a4]

sorteado = random.choice(alunos)
print(f'O ALUNO ESCOLHIDO FOI {sorteado}')