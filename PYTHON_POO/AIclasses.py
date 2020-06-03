# Criar duas classes, uma gerando um cliente e a outra recebendo o endereço desse cliente. No programa terá funções
# para inserir endereços e listar os endereços cadastrados. **Utilizar conceitos de Composição (POO).


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def adicionar_end(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def listar_end(self):
        for end in self.endereco:
            print(f'{end.cidade, end.estado}')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
