import random
import os

os.system('cls')

def sorteio(nomes):
    sortudo = random.choice(nomes)
    print(f'A pessoa sortuda é {sortudo}.')

nomes = []
for i in range(5):
    nomes.append(input(f'Digite o nome {i+1}/5°: '))

sorteio(nomes)
    
    
    