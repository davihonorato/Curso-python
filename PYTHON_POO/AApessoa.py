from time import sleep
from datetime import date


class Pessoa:
    ano_atual = date.today().year  # ano atual

    def __init__(self, nome, idade, falando=False, comendo=False):  # Método principal.
        # Variáveis podem ser importadas em qualquer função/scopo dentro da classe.
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def falar(self, assunto):  # Faz tal pessoa começar a falar sobre tal assunto.
        sleep(1)
        if self.falando:  # Caso a pessoa já esteja falando, o programa indica.
            print(f'{self.nome} já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo.') # Caso a pessoa esteja comendo, o programa indica.
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):  # Faz tal pessoa parar de falar (obviamente, apenas quando ela esteja falando).
        sleep(1)
        if not self.falando:  # Caso a pessoa não esteja falando, o programa indica.
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):  # Faz tal pessoa comer tal alimento.
        sleep(1)
        if self.comendo:
            print(f'{self.nome} já está comendo.')  # Caso a pessoa já esteja comendo, o programa indica.
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')  # Caso a pessoa esteja falando, o programa indica.
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        sleep(1)
        if not self.comendo:
            print(f'{self.nome} Não está comendo.')  # Caso a pessoa não esteja comendo, o programa indica.
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):  # Retorna o ano de nascimento com base na idade indicada.
        nascimento = self.ano_atual - self.idade
        return nascimento
