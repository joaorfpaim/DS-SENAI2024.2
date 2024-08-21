import os
import time

os.system('cls')

numeros = []
for x in range(10):
    numeros.append(int(input(f'Digite {1+x}/10 números inteiros: ')))
    os.system('cls')
    
media = sum(numeros)/len(numeros)
soma = sum(numeros)
time.sleep(0.4)

print(f'A soma dos números é {soma}, já a média dos é {media}')
