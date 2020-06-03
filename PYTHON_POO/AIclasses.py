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
            print(f'{end.cidade}-{end.estado}')

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}-{self.estado} FOI APAGADO')

# A "Composição" é definida quando determinada classe A, está contida na classe B e quando uma é apagada,
# a outra também será.
