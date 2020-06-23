# Criando uma classe através da metaclasse 'Type'


class Pai:
    nome = 'teste'


A = type('A', (Pai,), {'attr': 'Olá mundo!'})

a = A()
print(a.attr)
print(a.nome)