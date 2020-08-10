class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        print(valor)
        if isinstance(valor, str):
            a = valor.replace('R$', '')
            print(f'a: {a}')
            valor = float(a)
            print(f'valor: {valor}')
        self._preco = valor

    def desconto(self, porcentagem):
        print(self._preco, porcentagem)
        self._preco = self._preco - (self._preco * (porcentagem/100))
        print(self._preco)

    @nome.setter
    def nome(self, value):
        self._nome = value


# p1 = Produto('Teclado', 100)
p2 = Produto('Mouse', 'R$150')


# p1.desconto(10)
p2.desconto(10)
