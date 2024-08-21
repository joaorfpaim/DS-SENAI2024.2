import os
os.system('cls')

nomes = []
for x in range(5):
    nomes.append(input(f'Digite o {x+1}° nome: '))
    os.system('cls')
nomes.sort()
print(f'Os nomes em ordem alfabetica são {nomes}.')
