# Aqui será colocada o algorítmo da conta poupança.
from PYTHON_POO.AMconta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente.')

        self._saldo -= valor
