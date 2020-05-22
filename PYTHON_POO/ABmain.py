class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa.por_ano_nascimento('Davi', 2002)  # forma de obter os dados sem a idade
p2 = Pessoa('Luiz', 32)  # obtendo os dados com a idade
print(p1)
print(p1.nome, p1.idade)
print(p2)
print(p2.nome, p2.idade)
p1.get_ano_nascimento()
