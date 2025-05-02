"""

class NomeClasse:
    def __init__(self, parametro):
        self.atributo = parametro
    def metodo(self):
        #codigo

"""

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'{self.marca} {self.modelo} acelerou para {self.velocidade} Km/h')

    carro1 = Carro('Volks', 'Jetta')
    carro2 = Carro('Chevrolet', 'Cruze')

    carro1.acelerar(70)
    carro2.acelerar(50)