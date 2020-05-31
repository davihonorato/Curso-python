# Criar uma base de dados. O usuário pode adicionar, excluir e listar clientes (que possuem id e nome).
# *utilizar encapsulamento.


class Clientes:
    def __init__(self):
        self.lista = dict()

    def adicionar(self, id, nome):
        if 'clientes' not in self.lista:
            self.lista['clientes'] = {id, nome}
        else:
            self.lista['clientes'].upddate({id, nome})

    def listar_clientes(self):
        if 'clientes' not in self.lista:
            print('A lista está vazia.')
        else:
            for id, nome in self.lista['clientes'].items():
                print(id, nome)


user = Clientes()
user.adicionar(189, 'Davi')
user.listar_clientes()
