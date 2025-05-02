frase = input('Digite sua frase: ')

with open('frase.txt', "w") as arquivo:
    arquivo.write(frase)

with open('frase.txt', "r") as arquivo:
    conteudo = arquivo.read()
    print('Sua frase é:')
    print(conteudo)
