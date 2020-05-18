# Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a
# mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
# desafio 108.

import moeda

n = int(input('Digite um valor: R$'))
print(f'Para o número {moeda.moeda(n)}, nós podemos ter os seguintes valores: ')
print(f'AUMENTANDO 10% DE {moeda.moeda(n)} fica {moeda.aumentar(n, True)}')
print(f'DIMINUINDO 10% DE {moeda.moeda(n)} fica {moeda.diminuir(n, True)}')
print(f'O DOBRO DE {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A METADE DE {moeda.moeda(n)} é {moeda.metade(n, True)}')