class Pessoa:  # Superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):  # função de todas as classes
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):  # A classe "Cliente" herda tudo da classe "Pessoa". Classe filha
    def comprar(self):  # Função usada apenas para Cliente
        print(f'{self.nomeclasse} está comprando...')


class Aluno(Pessoa):  # A classe "Aluno" herda tudo da classe "Pessoa". Classe filha
    def estudar(self):  # Função usada apenas para Aluno
        print(f'{self.nomeclasse} está estudando...')
