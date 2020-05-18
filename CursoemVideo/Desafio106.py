# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use
# cores.


def função(com):
    help(com)


comando = ''
while True:
    comando = str(input('FUNÇÃO OU BIBLIOTECA >> ')).lstrip().rstrip()
    if comando.upper() == 'FIM':
        break
    else:
        função(comando)
