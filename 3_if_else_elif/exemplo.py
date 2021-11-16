usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

usuario_db = 'usuariobd'
senha_db = 123456

if usuario == usuario_db and int(senha) == senha_db:
    print(f'Você está logado.')
else:
    print(f'Usuário e/ou senha não corresponde.')
