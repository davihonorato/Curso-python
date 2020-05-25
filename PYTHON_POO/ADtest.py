# Tentando desenvolver algum exercício que pratique o que foi ensinado na aula.
class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def adicionar(self):
        verificar('ADlista.txt')
        n = open('ADlista.txt', 'at')
        pessoa = list()
        pessoa.append(self.nome)
        pessoa.append(str(self.nascimento))
        n.writelines(pessoa)
        n.close()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        self._nome = name.capitalize()

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 0 <= ano <= 20:
            self._nascimento = 2000 + ano
        elif 20 < ano < 100:
            self.nascimento = 1900 + ano
        else:
            self._nascimento = ano


def verificar(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except:
        open(arquivo, 'wt+')
    else:
        arq.close()


p1 = Pessoa('Davi', 2002)
p1.adicionar()
