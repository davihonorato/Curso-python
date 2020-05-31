# Criar uma base de dados. O usuário pode adicionar, excluir e listar clientes (que possuem id e nome).
# *utilizar encapsulamento.


class Clientes:
    def __init__(self):
        self.__lista = {}  # Recomenda-se estritamente não modificar essa variável

    def adicionar_cliente(self, id, nome):
        if 'clientes' not in self.__lista:
            self.__lista['clientes'] = {id: nome}
        else:
            self.__lista['clientes'].update({id: nome})

    def listar_clientes(self):
        if 'clientes' not in self.__lista:
            print('A lista está vazia.')
        else:
            for id, nome in self.__lista['clientes'].items():
                print(id, nome)

    def deletar_cliente(self, id):
        del self.__lista['clientes'][id]


user = Clientes()
user.adicionar_cliente(189, 'Davi')
user.adicionar_cliente(123, 'yan')
user.adicionar_cliente(198, 'lorena')
user.__lista = 'Outra coisa'  # Variável criada pelo programa. Caso queira acessar
# a variável da classe, terá que instanciar da seguinte forma: user._Pessoas__lista
user.listar_clientes()
user.deletar_cliente(123)
user.listar_clientes()
