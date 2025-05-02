import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Tente adivinhar o número entre 1 e 100.")
print("Digite 'x' para sair a qualquer momento.")

while not acertou:
    chute = input("Digite o seu palpite: ")
    
    if chute.lower() == "x":
        print(f"Programa encerrado! Você desistiu com {tentativas} tentativas")
        break
    
    if not chute.isdigit():
        print("Por favor, digite um número válido ou 'x' para sair")
        continue

    chute = int(chute)
    tentativas += 1

    if chute == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif chute < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
