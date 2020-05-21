# Criar um programa que utilize classes e métodos da linguagem Python. Utilizando as tecnicas de classes,
# "crie" pessoas com nome e idade, e terá que inidicar se estão falando ou não e comendo ou não.
# Tudo será instanciado.
# - Se está falando, não pode falar de outro assunto e não pode comer. Se não está falando, não pode parar de falar.
# - Se está comendo, não pode comer outro alimento e não pode falar. Se não está comendo, não pode parar de comer.
# Criar também um método que retorne o ano de nascimento da pessoa.

from PYTHON_POO.AApessoa import Pessoa  # Importa a classe

p1 = Pessoa('Davi', 18)
p1.falar('animes')
p1.falar('series')
p1.parar_falar()
p1.falar('series')
p1.comer('biscoito')
p1.parar_falar()
p1.comer('biscoito')
p1.falar('maçã')
p1.parar_comer()
print(Pessoa.ano_atual)  # Imprime o ano atual
print(p1.get_ano_nascimento())  # Ano de nascimento de p1

