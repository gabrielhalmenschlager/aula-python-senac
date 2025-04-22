estoque = {}

while True:
    nome = input("Digite o nome do produto (fim para finalizar): ")

    if nome.lower() == "fim":
        print("\nPrograma encerrado! Estoque final:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")
        break

    quantidade_est = int(input("Digite a quantidade: "))

    if not quantidade_est.isdigit():
        print("Por favor, digite uma quantidade válida.\n")
        continue

    quantidade = quantidade_est
    estoque[nome] = quantidade
