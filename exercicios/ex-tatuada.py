numero = int(input("\nDigite um número entre 0 e 10: "))

# Usando While
print('\nUsando WHILE')

if 0 <= numero <= 10:
    print(f"\nTabuada do {numero}:")
    
    multiplicador = 1

    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1

else:
    print("Digite um número entre 0 e 10!")

print('\n')

# Usando For
print('Usando FOR')

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")