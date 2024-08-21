#Estrutura de repeticão

import os
"""
#Ex 1
for x in range(3,20,2):
    print(x)

x é o ponteiro de mudança 
o primeiro número dentro dos parenteses é o valor inicial
o segundo é o limite
o terceiro são os passos
"""

"""
Ex 2
numeros = [22,33,67,44,56,81,11,12]


for x in range(len(numeros)):
    if numeros[x]%2==0:
        print(numeros[x])
"""

#Ex 3
numeros = []
for x in range(5):
    n = numeros.append(int(input('Digite um número: ')))
    if numeros[x] % 2 == 1:
        numeros.append(n)
print(numeros)
    