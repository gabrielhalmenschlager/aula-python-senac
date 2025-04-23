senha = input("Digite sua senha: ")

if len(senha) < 8:
    print("Senha muito curta.")

elif senha.lower() == senha:
    print("Falta uma letra maiúscula.")

elif not any(tem_numero.isdigit() for tem_numero in senha):    
    print("Falta um número.")

elif not any(tem_minuscula.islower() for tem_minuscula in senha):
    print("Falta uma letra minúscula.")

else:
    print("Senha válida!")

'''

senha = input("Digite sua senha: ")

temMaiscula = False
temNumero = True

if len(senha) < 8:
    print('A senha dever ter pelos menos 8 caracteres')
else:
    for char in senha:
        if char.isUpper():
            temMaiscula = True
        if char.isDigit():
            temNumero = True
    if temMaiscula and temNumero:
        print('Senha válida!')
    else:
        print('A senha deve conter pelo menos uma letra maiuscula e um numero')

'''