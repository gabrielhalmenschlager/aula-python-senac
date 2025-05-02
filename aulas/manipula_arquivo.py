# Cria ou substitui o arquivo e escreve duas linhas nele
with open('../documentos-textos/texto.txt', "w") as arquivo:
    arquivo.write('Linha 1: Ola, Mundo!\n')
    arquivo.write('Linha 2: Python e show.\n')

# Abre o arquivo para leitura e mostra todo o conteúdo
with open('../documentos-textos/texto.txt', "r") as arquivo:
    conteudo = arquivo.read()
    print('Conteudo do arquivo:')
    print(conteudo)

# Lê o arquivo linha por linha e imprime cada uma sem quebras de linha extras
with open('../documentos-textos/texto.txt', "r") as arquivo2:
    for linha in arquivo2:
        print(linha.strip())
