class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base*self.altura)/2

t = Triangulo(5, 6)
print("A área do triângulo é: {}m²".format(t.area()))