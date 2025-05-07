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

except Exception as e:
    print(f'Erro ao criar arquivo: {e}')
