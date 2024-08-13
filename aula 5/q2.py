nome = input('Qual é a sua nome: ')
idade = int(input(f'Ola, {nome}, quantos ano você tem?: '))

if idade < 13:
    print(f'{nome}, você é uma criança.')
elif idade > 12 and idade < 18:
    print(f'{nome}, você é um adolescente.')
elif idade > 17 and idade < 60:
    print(f'{nome}, você é um adulto.')
else:
    print(f'{nome}, você é um idoso.')