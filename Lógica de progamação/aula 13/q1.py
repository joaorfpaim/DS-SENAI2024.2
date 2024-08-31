import time
import os
os.system('cls')


def calculo(peso):
    if peso > 50:
        multa = (peso - 50)*4
        print(f'Você tera que pagar uma multa de {(peso - 50)*4}R$')
    

peso = int(input('Qual é o peso em KG: '))

if peso > 50:
    print(f'O peso excede {peso - 50}KG do estabelecido pelo regulamento.')

time.sleep(1)
calculo(peso)
