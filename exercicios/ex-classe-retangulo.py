
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        if self.largura > 0 and self.altura > 0:
            area = self.largura * self.altura
            print(f'A área do retangulo é {area}')
        else:
            print('Valores invalidos')

calculoArea = Retangulo(4, 5)
calculoArea.area()
