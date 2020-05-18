# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: Mostrar o calculo (opcional).
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c}', end=' ')
            if c != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


n = int(input('Digte um número para obter o fatorial: '))
print(fatorial(n))
