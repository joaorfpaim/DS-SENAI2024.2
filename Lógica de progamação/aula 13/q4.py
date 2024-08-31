import os
os.system('cls')

numeros = []

def calculo(numeros):
    soma = sum(numeros)    
    media = (sum(numeros))/5
    print(f'A soma dos números deu {soma} e a média {media}')
for i in range(5):
    numeros.append(int(input(f'Digite o {i + 1}° número: ')))
    
calculo(numeros)
    
