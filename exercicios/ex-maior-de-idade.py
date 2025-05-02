nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print(f'Seu nome é {nome} e sua idade é {idade}, Você é maior de idade!')
else:
    print(f'Seu nome é {nome} e sua idade é {idade}, Você é menor de idade!')