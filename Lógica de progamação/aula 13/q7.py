import os
os.system('cls')

def preco(km):
    dias = int(input('Digite por quantos dias você alugou o carro: '))
    valor = (dias*60) + (km*0.15)
    print(f'O valor a pagar é de {valor:.2f}R$')
km = int(input('Digite quantos Km/h você rodou com o carro: '))

preco(km)