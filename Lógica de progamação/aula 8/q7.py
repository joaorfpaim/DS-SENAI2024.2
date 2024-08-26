import os
import time
os.system('cls')

numneg = []
numpos = []

for x in range(10):
    n = int(input(f'Digite o valor n°{x+1}: '))
    os.system('cls')
    if n>0:
        numpos.append(n)
    else:
        numneg.append(n)
time.sleep(1)
print(f'A quantidade de números positivos é {len(numpos)}')
print(f'A quantidade de números positivos é {len(numneg)}')

time.sleep(60)
os.system('cls')
