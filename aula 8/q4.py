import os
os.system('cls')

nomes = []
for i in range(5):
    nomes.append(input(f'Digite o {i+1}° nome: '))
    os.system('cls')
nomes.sort()

print('Os nomes em ordem alfabetica são:')
for i in nomes:
    print(i)
