from abc import ABC, abstractmethod


class A(ABC):  # Superclasse
    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    def falar(self, msg):  # possui a mesma quantidade e o mesmo tipo de parâmertos que a classe A
        print(f'B está falando {msg}')


class C(A):  # possui a mesma quantidade e o mesmo tipo de parâmertos que a classe A
    def falar(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.falar('UMA MENSAGEM')
c.falar('OUTRA MENSAGEM')
