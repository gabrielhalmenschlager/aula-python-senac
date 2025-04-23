senha = input("Digite sua senha: ")

if len(senha) < 8:
    print("Senha muito curta.")

elif senha.lower() == senha:
    print("Falta uma letra maiúscula.")

elif not any(tem_numero.isdigit() for tem_numero in senha):    
    print("Falta um número.")

else:
    print("Senha válida!")
