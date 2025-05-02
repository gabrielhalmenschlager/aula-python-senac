texto = 'Lorem ipsum dolor sit amet. Eos magni ducimus At eveniet aliquid a vitae iste rem iste temporibus. Et recusandae consequatur in iste dolorem cum esse nemo ex fuga sint id magni adipisci id aperiam eius quo incidunt pariatur. Qui magnam consequatur ut galisum sunt vel dolorem esse aut vero aspernatur. Eum nesciunt cumque 33 illum eveniet non necessitatibus quasi est laudantium neque ea similique magnam. </p><p>Est aspernatur rerum in pariatur iste qui blanditiis praesentium ex laboriosam eius ut quis voluptatem. Et laudantium culpa et quia blanditiis et unde nemo eum perferendis nihil! </p><p>In error dignissimos vel porro velit ut molestiae dignissimos quo laudantium mollitia et tempora totam nam sint cumque. A facere dignissimos et nesciunt consectetur non iusto iusto qui voluptates autem in incidunt galisum eum enim voluptas. Sit veniam architecto aut nesciunt omnis et pariatur doloremque? Non molestiae numquam id voluptatem ullam eum soluta laborum est odit asperiores qui galisum vero.'

with open('textoatv14.txt', "w") as arquivo:
    arquivo.write(texto)

contagem = {}

with open('textoatv14.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        palavras = linha.split()

        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1

print("Contagem de palavras:")
for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")

'''

try:
    with open('textoatv14.txt', 'r') as arquivo:
        texto = arquivo.read().lower()
        palavras = texto.split()
        contagem = {}

        for palavra in palavras:
            contagem[palavra] = contagem.get(palavra, 0) + 1
            print(contagem)

except FileExistsError:
    print('Erro, arquivo nao existe')

'''