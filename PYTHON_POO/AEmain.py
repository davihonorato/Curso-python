# Atribudos de classes
# Mudar o valor da váriavel de classe
class A:
    vc = 123  # Variável de classe

    def __init__(self):
        self.vc = 321  # Variável de instância (muda apenas na instância)


a1 = A()
a2 = A()
# A.vc = 321 --> opção para mudar todas as variáveis 'vc'.

print(a1.vc)
print(a2.vc)
print(A.vc)
