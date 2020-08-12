class Biblioteca:
    def __init__(self):
        self.lista = {}

    def adiconar(self, titulo):
        if 'jogos' not in self.lista:
            self.lista['jogos'] = {titulo}
            print('#######')
            for j in self.lista['jogos']:
                print(j.nome, j.ano)
        else:
            if titulo in self.lista:
                print(f'{titulo.nome} já está na lista.')
                return

            self.lista['jogos'].update(titulo)
            print('#######')
            print(self.lista)


class Jogo:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano


arq1 = Jogo('Revil', 2002)
estante = Biblioteca()

estante.adiconar(arq1)
