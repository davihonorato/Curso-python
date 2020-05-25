class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * (porcentagem/100))
        print(self.preco)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Caderno', 100)
p2 = Produto('Borracha', 'R$20')
p1.desconto(10)
p2.desconto(10)
