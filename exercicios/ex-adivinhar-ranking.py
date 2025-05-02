import random

"""

nome = input('Digite seu nome: ')

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False
ranking = []

def ler_ranking():
    try:
        with open("ranking.txt", "r") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return []

print("Tente adivinhar o número entre 1 e 100.")
print("Digite 'x' para sair a qualquer momento.")

while not acertou:
    chute = input("Digite o seu palpite: ")

    if chute.lower() == "x":
        print(f"Programa encerrado! Você desistiu com {tentativas} tentativa(s).")
        break

    if not chute.isdigit():
        print("Por favor, digite um número válido ou 'x' para sair.")
        continue

    chute = int(chute)
    tentativas += 1

    if chute == numero_secreto:
        acertou = True
        print(f"\nParabéns, {nome}! Você acertou em {tentativas} tentativa(s)!")

        ranking = ler_ranking()
        
        ranking.append(f"{nome} - {tentativas} tentativa(s)\n")

        print("\nRanking Atual (em ordem crescente de tentativas):")
        for idx, jogador in enumerate(ranking, 1):
            print(f"{idx}. {jogador.strip()}")

        with open("ranking.txt", "w") as arquivo:
            for jogador in ranking:
                arquivo.write(jogador)
    elif chute < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

"""

ranking = []

# Leitura do ranking
try:
    with open('rankink.txt', 'r') as arquivo:
        for linha in arquivo:
            try:
                nomeJogador, resto = linha.strip().split(': ')
                tentativasJogador = int(resto.split()[0])
                ranking.append((nomeJogador, tentativasJogador))
            except (ValueError, IndexError):
                continue
except FileNotFoundError:
    pass

# Jogo
numeroSecreto = random.randint(1, 100)
tentativas = 0
nome = input('Digite seu nome: ')

while True:
    palpite = input('Digite seu palpite (1 a 100): ')
    tentativas += 1

    try:
        palpite = int(palpite)
        if palpite < 1 or palpite > 100:
            print('Erro: número fora do intervalo.')
            continue

        if palpite == numeroSecreto:
            print(f'Parabéns, você acertou em {tentativas} tentativas!')
            break
        elif palpite < numeroSecreto:
            print('O número é maior.')
        else:
            print('O número é menor.')
    except ValueError:
        print('Erro: digite um número válido.')

# Atualiza ranking
ranking.append((nome, tentativas))

with open('rankink.txt', 'w') as arquivo:
    for nomeJogador, tentativasJogador in ranking:
        arquivo.write(f'{nomeJogador}: {tentativasJogador} tentativas\n')

# Mostra ranking ordenado
rankingOrdenado = sorted(ranking, key=lambda x: x[1])
print('\n=== Ranking de Jogadores ===')
if rankingOrdenado:
    for pos, (nomeJogador, tentativasJogador) in enumerate(rankingOrdenado, start=1):
        print(f'{pos}. {nomeJogador}: {tentativasJogador} tentativas')
else:
    print('Nenhum ranking encontrado.')
