import os
os.system('cls')

compras = []

def somar(compras):
    soma = sum(compras)
    print(f'O valor total da compra é {soma:.2f} ')

while True:
    preco = float(input('Digite o valor do produto: '))
    if preco == -1:
        break
    compras.append(preco)

somar(compras)

os.system('cls')
