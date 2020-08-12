class Biblioteca:
    def __init__(self):
        self.lista = {}

    def adicionar(self, titulo):  # Adiciona um jogo à lista
        if 'jogos' not in self.lista:
            self.lista['jogos'] = {titulo}
        else:
            if titulo in self.lista:
                print(f'{titulo.nome} já está na lista.')
                return

            self.lista['jogos'].update({titulo})

    def apagar(self, titulo):  # Apaga um ítem da lista
        pass

    def mostrar(self):  # Mostra na tela uma lista com todos os jogos
        for tit in self.lista['jogos']:
            print(f'| {tit.nome:<15}  {"-":^2}  {tit.ano:>5} |')


class Jogo:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano


arq1 = Jogo('Resident evil', 2002)
arq2 = Jogo('Bully', 2004)
arq3 = Jogo('Castlevania', 2013)
estante = Biblioteca()

estante.adicionar(arq1)
estante.adicionar(arq2)
estante.adicionar(arq3)
estante.mostrar()
