
"""

with open('numeros.txt', "w") as arquivo:
    arquivo.write('10.1\n')
    arquivo.write('20.2\n')
    arquivo.write('30.3\n')
    arquivo.write('40.4\n')
    arquivo.write('50.5\n')

soma = 0
quantidade = 0

try:
    with open("numeros.txt") as arquivo:
        for linha in arquivo:
            try:
                num = float(linha)
                soma += num
                quantidade += 1
            except ValueError:
                print(f"Valor inválido")

    if quantidade > 0:
        media = soma / quantidade
        print(f"Média: {media:.2f}")
    else:
        print("Nenhum número válido encontrado.")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print(f"Erro: {e}")

"""

try:
    with open('../documentos-textos/numeros.txt', 'r') as arquivo:
        numeros = []
        for linha in arquivo:
            try:
                numeros.append(float(linha.strip()))
            except ValueError:
                continue

        if numeros:
            media = sum(numeros) / len(numeros)
            print(f'Média: {media:.2f}')
        else:
            print('Nenhun número encontrado')

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")