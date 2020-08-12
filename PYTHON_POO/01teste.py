class Biblioteca:
    def __init__(self):
        self.lista = {}  # {'jogos:{n1: a1}, {n2, a2}, {n3, a3}}

    def adicionar(self, titulo):  # Adiciona um jogo à lista
        if 'jogos' not in self.lista:
            self.lista['jogos'] = {titulo.nome: titulo.ano}
        else:
            if titulo in self.lista:
                print(f'{titulo.nome} já está na lista.')
                return

            self.lista['jogos'].update({titulo.nome: titulo.ano})

    def apagar(self, titulo):  # Apaga um ítem da lista
        if titulo.nome in self.lista['jogos']:
            del self.lista['jogos'][titulo.nome]
        else:
            print('O jogo não existe na lista.')

    def mostrar(self):  # Mostra na tela uma lista com todos os jogos
        for nome, ano in self.lista['jogos'].items():
            print(f'| {nome:<15}  {"-":^2}  {ano:>5} |')


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
estante.apagar(arq1)
print(' ---------------------------- ')
estante.mostrar()

