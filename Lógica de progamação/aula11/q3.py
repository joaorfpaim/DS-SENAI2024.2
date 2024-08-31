import os   
os.system('cls')

num = []
for i in range(6):
    num.append(int(input(f'Digite o {i+1} valor: ')))

def par (num):
    cont = 0
    for i in num:
        if i%2 == 0:
            cont = cont + 1
    return cont

print(f'A quantidade de números pares é {par(num)}')