texto = '   Olá, mundo!   '

# Converte todas as letras para maiúsculo
print(texto.upper())

# Converte todas as letras para minúsculo
print(texto.lower())

# Remove todos os espaços em branco
print(texto.strip())

texto2 = 'Python é divertido, pois é muito legal'

# Separa a frase em palavras, formando uma lista
palavras = texto2.split()
print(palavras)

# Junta as palavras com hífens no lugar dos espaços
texto3 = '-'.join(palavras)
print(texto3)

texto4 = 'Python é divertido'

# Troca a palavra "divertido" por "incrível"
print(texto4.replace('divertido', 'incrivel'))