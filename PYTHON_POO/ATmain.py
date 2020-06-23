'''class Meta(type):
    pass
'''

class A:
    def fala(self):
        self.b_fala()


class B(A):
    def b_fala(self):
        print('Classe de B')


b1 = B()
b1.fala()
