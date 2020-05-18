# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

import moeda

n = int(input('Digite um valor: R$'))
print(f'Para o número {moeda.moeda(n)}, nós podemos ter os seguintes valores: ')
print(f'AUMENTANDO 10% DE {moeda.moeda(n)} fica {moeda.moeda(moeda.aumentar(n))}')
print(f'DIMINUINDO 10% DE {moeda.moeda(n)} fica {moeda.moeda(moeda.diminuir(n))}')
print(f'O DOBRO DE {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A METADE DE {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
