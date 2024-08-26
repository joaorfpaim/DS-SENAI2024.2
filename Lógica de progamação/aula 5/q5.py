login = input(('Digite seu nome de usuario: '))
senha = (input(f'{login}, Digite sua senha: '))
senhacor = 'python123'
if senha == senhacor:
    print("Acesso permitido")
else:
    print("Acesso negado")