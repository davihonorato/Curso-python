# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie
# uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de
# dados para aceitar apenas valores que seja monetários.

from CursoemVideo.Desafio112.utilidadesCeV import dados, moeda

n = dados.leiaDinheiro('Digite um valor: R$')
moeda.resumo(n, 45, 28)