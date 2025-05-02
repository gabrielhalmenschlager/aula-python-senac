try:
    numero = int(input('Digite um numero: '))
    resultado = 10 / numero
    print(resultado)
    
except ZeroDivisionError:
    print('Erro: Divisão por zero!')
except ValueError:
    print('Erro: Digite um numero valido!')