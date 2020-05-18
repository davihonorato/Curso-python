# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('BANANA', 'PYTHON', 'BATATA', 'AMOR', 'AZUL', 'PRETO', 'DOR', 'FELICIDADE', 'AMARELO', 'COMPUTADOR', 'AMIZADE', 'ANIME', 'JOGOS', 'PROGRAMADOR')

for c in palavras:
    print(f'\n{c}:', end=' ')
    for n in c:
        if n in 'AEIOU':
            print(n, end=' ')

# muito interessante esse exercício, pois aborda cada detalhe dos comandos.
