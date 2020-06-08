class LogMixin: # Características: Classe auxiliar do programa
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:  # É necessário uma extensão no Pycharm
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


class Dispositivo:  # Características: Classe secundária do programa; classe super
    def __init__(self, modelo):
        self._modelo = modelo
        self.ligado = False

    def ligar(self):
        if self.ligado:
            return

        self.ligado = True

    def desligar(self):
        if not self.ligado:
            return

        self.ligado = False


class Smastphone(Dispositivo, LogMixin):  # Características: Classe principal do programa; classe filha
    def __init__(self, modelo):
        super().__init__(modelo)
        self.conectado = False

    def conectar(self):
        if not self.ligado:
            error = f'{self._modelo} ESTÁ desligado.'
            print(error)
            self.log_error(error)
            return
        if self.conectado:
            info = f'{self._modelo} já está conectado.'
            print(info)
            self.log_info(info)
            return

        self.conectado = True
        info = f'{self._modelo} foi conectado.'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self.conectado:
            error = f'{self._modelo} NÃO está conectado.'
            print(error)
            self.log_error(error)
            return

        self.conectado = False
        info = f'{self._modelo} foi desconectado.'
        print(info)
        self.log_info(info)
