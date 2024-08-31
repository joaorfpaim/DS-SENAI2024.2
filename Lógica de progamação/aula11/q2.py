import os
import time

os.system('cls')

# Código
valores = []

for i in range(3):
    valores.append(int(input(f'Digite o {i+1}° valor: ')))

def maior (valores):
    maior = max(valores)
    time.sleep(2)
    print(f'O maior valor, dentre os três é {maior}')
    
maior(valores)  


time.sleep(10)
os.system('cls')
