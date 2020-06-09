# Será criado uma classe abstrata que serve como "classe principal" para as outras.

from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.getter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor precisa ser numérico.')

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor precisa ser numérico.')

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'AGENCIA: {self._agencia}', end=' | ')
        print(f'CONTA: {self._conta}', end=' | ')
        print(f'SALDO: {self._saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
