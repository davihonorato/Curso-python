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
