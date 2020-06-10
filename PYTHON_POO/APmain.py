class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # Possibilita que os objetos sejam testados (com "==") para saber se são iguais
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
print(r1 == r2)  # Testando o método __eq__
