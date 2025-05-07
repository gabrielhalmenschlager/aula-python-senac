import csv
import os

class Estudante:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Em recuperação'
        else:
            return 'Reprovado'

    def exibirRelatorio(self):
        media = self.calcular_media()
        status = self.verificar_aprovacao()
        print(f"Nome: {self.nome}")
        print(f"Notas: {self.notas}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")
        print("-" * 30)

    def ler_estudantes():
        caminho_arquivo = '../documentos-textos/alunos.csv'
        os.makedirs('../documentos-textos', exist_ok=True)
        try:
            with open(caminho_arquivo, 'r', newline='') as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor) 
                for linha in leitor:
                    nome = linha[0]
                    notas = list(map(float, linha[1:]))
                    estudante = Estudante(nome, notas)
                    estudante.exibirRelatorio()

        except FileNotFoundError as e:
            print(f'Erro ao acessar o arquivo: {e}')

Estudante.ler_estudantes()