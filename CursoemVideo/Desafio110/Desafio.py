# Exercício Python 110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from CursoemVideo.Desafio110 import moeda

n = int(input('Digite um valor: R$'))
moeda.resumo(n, 80, 20)
