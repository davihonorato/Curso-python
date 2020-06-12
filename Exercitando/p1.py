class Login:
    def __init__(self, nome, servico='normal'):
        self._nome = nome
        self._servico = servico
        self._musica = None

    @property
    def nome(self):
        return self._nome

    @property
    def servico(self):
        return self._servico

    @property
    def musica(self):
        return self._servico

    @musica.setter
    def musica(self, value):
        self._musica = value


class App:
    @staticmethod
    def tocar(musica):
        print(f'Está tocando {musica}')


user = Login('Davi')
player = App()
user.musica = player
user.musica.tocar('Creep')
