# PRIMEIRA FORMA DE CRIAR UM GERENCIADOR DE CONTEXTO
"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo o arquivo...')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando o arquivo...')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando o arquivo...')
        self.arquivo.close()


with Arquivo('AR.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
"""

# SEGUNDA FORMA DE CRIAR UM GERENCIADOR DE CONTEXTO
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo...')
        arq = open(arquivo, modo)
        yield arq  # retorna o arquivo para aberto
    finally:
        print('Fechando o arquivo...')
        arq.close()


with abrir('AR.txt', 'w') as arquivo:
    arquivo.write('LINHA 1\n')
    arquivo.write('LINHA 2\n')
    arquivo.write('LINHA 3\n')
