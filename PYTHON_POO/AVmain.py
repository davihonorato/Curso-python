class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta=None):
        Pessoa.__init__(self, nome, idade)
        pass


class Conta:
    def __init__(self, agencia, numConta, saldo):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo

    def depositar(self, quantia):
        pass


class ContaCorrente:
    pass


class ContaPoupanca:
    pass
