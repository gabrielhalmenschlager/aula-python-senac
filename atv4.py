numero1 = float(input("\nDigite o número um: "))
numero2 = float(input("Digite o número dois: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
    print('\nA operação é válida')

    if operacao == "+":
        resultado = numero1 + numero2
        print(f'\nA operação é uma adição: {numero1} {operacao} {numero2} = {resultado}')

    elif operacao == "-":
        resultado = numero1 - numero2
        print(f'\nA operação é uma subtração: {numero1} {operacao} {numero2} = {resultado}')

    elif operacao == "*":
        resultado = numero1 * numero2
        print(f'\nA operação é uma multiplicação: {numero1} {operacao} {numero2} = {resultado}')

    elif operacao == "/":
        if numero2 == 0:
            print('\nDivisão por zero não pode ser realizada')
        else:
            resultado = numero1 / numero2
            print(f'\nA operação é uma divisão: {numero1} {operacao} {numero2} = {resultado}')
else:
    print('\nA operação não é válida')
