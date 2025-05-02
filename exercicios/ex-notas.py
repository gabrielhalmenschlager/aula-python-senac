nota = float(input('Digite sua nota: '))

if nota <= 0 or nota <= 10:
    print(f'Nota valida {nota}')
    if nota > 6:
        print(f'O aluno foi APROVADO com a nota: {nota}')
    elif nota >= 5:
        print(f'O aluno foi esta de RECUPERAÇÂO com a nota: {nota}')
    else:
        print(f'O aluno foi REPROVADO com a nota: {nota}')
else:
    print(f'Nota invalida {nota}')