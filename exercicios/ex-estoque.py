estoque = {}

while True:
    nome = input("Digite o nome do produto (fim para finalizar): ")

    if nome.lower() == "fim":
        print("\nPrograma encerrado! Estoque final:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")

        if estoque:
            maior_produto = max(estoque, key=estoque.get)
            maior_quantidade = estoque[maior_produto]
            print(f"\nProduto com mais quantidade: {maior_produto}, quantidade: {maior_quantidade}")
            
            total_itens = sum(estoque.values())
            print(f"Quantidade total no estoque: {total_itens}")
        break

    quantidade_est = input("Digite a quantidade: ")

    if not quantidade_est.isdigit():
        print("Por favor, digite uma quantidade válida.\n")
        continue

    quantidade = int(quantidade_est)
    estoque[nome] = quantidade
