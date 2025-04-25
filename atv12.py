palavra = input("Digite uma palavra: ")

contagem = {}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1
        
print(f"Contagem das letras: {contagem}")
