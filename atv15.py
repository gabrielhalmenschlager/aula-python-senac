import random

nome = input('Digite seu nome: ')

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False
ranking = []

# Função para ler o ranking do arquivo
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
