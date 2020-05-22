from random import randint


class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):  # referente à instância
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # referente à instância
        print(self.ano_atual - self.idade)

    @classmethod  # é referente a classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # Não é referente nem à instância e nem à classe. Funciona como se fosse uma função normal
    def gerar_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Luiz', 32)
print(Pessoa.gerar_id())  # gera um id para uma pessoa
print(p1.gerar_id())  # gera um id para a pessoa p1 (mas sem armazenar em algum canto)
