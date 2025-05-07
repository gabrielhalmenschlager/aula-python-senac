
import csv
import os

alunos = [
    ['Nome', 'Nota'],
    ['Gabriel', 8.0],
    ['Luiz', 7.0]
]

os.makedirs('../documentos-textos', exist_ok=True)

try:
    with open('../documentos-textos/alunos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(alunos)
    print('Arquivo criado com sucesso!')

    with open('../documentos-textos/alunos.csv', 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            nome, nota = linha
            print(f'{nome}: {nota}')

except FileNotFoundError as e:
    print(f'Erro ao criar arquivo: {e}')
