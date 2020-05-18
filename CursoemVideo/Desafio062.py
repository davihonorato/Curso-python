# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que
# quer mostrar 0 termos.

print('---PROGRESSÃO ARITMÉTICA---')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1  # Contador do programa
n = 10  # Quantidade de termos na PA
resp = n  # O pedido inicial do usuário são 10 números
termo = a1  # Uma variável para se atualizar.
while resp != 0:
    while c <= n:
        print(f'{termo}', end='')
        print(f' -> ' if c != n else '', end='')
        termo += r
        c +=1
    resp = int(input('\nVocê quer mostrar mais quantos termos? '))
    n += resp
print(f'\nA progressão foi finalizada com {n} termos.')
