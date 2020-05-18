# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

# Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a
# mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
# desafio 108.


def aumentar(x, formato=False):
    valor = x + (x*.10)
    return valor if not formato else moeda(valor)


def diminuir(x, formato=False):
    porc = x * 0.10
    valor = x - porc
    return valor if formato is False else moeda(valor)


def dobro(x, formato=False):
    dobro = x * 2
    return dobro if not formato else moeda(dobro)


def metade(x, formato=False):
    met = x/2
    return met if formato is False else moeda(met)

def moeda(x, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')
