usuario = input('Digite o seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Digite um usuário com pelo menos 6 dígitos.')
else:
    senha = input('Digite sua senha: ')
    print('Você foi cadastrado com sucesso!')

print(f'O total de caracteres digitados foi: {len(usuario) + len(senha)}')
