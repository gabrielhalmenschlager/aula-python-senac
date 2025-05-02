numeros = []

while True:
    entrada = input("Digite um número (fim para finalizar): ")

    if entrada.lower() == "fim":
        print(f"\nPrograma encerrado! Você digitou: {numeros}")
        
        if numeros:
            media = sum(numeros) / len(numeros)
            print(f"A média dos números é: {media:.2f}")
        else:
            print("Nenhum número foi inserido.")
        break

    if not entrada.isdigit():
        print("Por favor, digite um número válido.\n")
        continue

    numero = int(entrada)
    numeros.append(numero) 