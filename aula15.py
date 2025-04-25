try:
    with open('naoexiste.txt', 'r') as arquivo:
        print(arquivo.read())

except:
    print('Erro')