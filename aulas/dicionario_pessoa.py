pessoa = {
         'nome': 'Gabriel',
         'idade': 17,
         'cidade': 'scs'
         }

print(pessoa)

print(pessoa['nome'])

pessoa['cpf'] = '123.456.789-10'
pessoa['nome'] = 'João'

print(pessoa)

del pessoa ['cidade']

print(pessoa)
