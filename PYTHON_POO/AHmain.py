from PYTHON_POO.AHclasses import *

carrinho = CarrinhoDeCompras()
p1 = Produto('caneta', 2)
p2 = Produto('lapis', 1)
p3 = Produto('borracha', 1)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.listar_produtos()
print(carrinho.soma_total())
