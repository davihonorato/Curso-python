# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Média 7.0 ou superior: APROVADO.
from time import sleep

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1+n2)/2
print('\033[35mProcessando...')
sleep(1)

if media <= 5.0:
    print(f'\033[31mREPROVADO! \nMÉDIA: {media}')
elif media > 5.0 and media < 6.9:
    print(f'\033[34mRECUPERAÇÃO! \nMÉDIA: {media}!')
else:
    print(f'\033[32mAPROVADO! \nMÉDIA: {media}')