'''
A Guide to Python's Magic Methods: https://rszalski.github.io/magicmethods/
'''


class A:
    def __new__(cls, *args, **kwargs):  # É executado antes do init. argumentos: *args, argumentos nomeados: **kwargs.
        return super().__new__(cls)  # permite que o init seja executado (pesquisar sobre)

    def __init__(self):  # "Inicializador" da classe
        print('Eu sou o INIT')

    def __del__(self):  # Finaliza o programa do python. Às vezes pode não executar.
        print('Conteúdo coletado.')


a = A()
