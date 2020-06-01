# Criar um carrinho de compras que possa realizar algumas ações com determinado produto. Pode-se 1- adicionar o produto
# no carrinho, 2- listar os produtos no carrinho e 3- somar o total dos preços.
# Agregação


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = list()

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(p.nome, p.valor)

    def soma_total(self):
        total = 0
        for p in self.produtos:
            total += p.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
