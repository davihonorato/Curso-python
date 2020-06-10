class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def area(self):
        return self.x * self.y

    def __eq__(self, other):  # Possibilita que os objetos sejam testados (com "==") para saber se são iguais
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.area()
        a2 = other.area()

        if a1 > a2:
            return True
        else:
            return False

    def __lt__(self, other):
        a1 = self.area()
        a2 = other.area()

        if a1 < a2:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
print(r1)  # Testando o método __repr__
print(r2)  # Testando o método __repr__
print(r1 == r2)  # Testando o método __eq__
print(r1 > r2)  # Testando o método __gt__
print(r1 < r2)  # Testando o método __lt__
