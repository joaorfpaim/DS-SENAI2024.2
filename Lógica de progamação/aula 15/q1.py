import os
os.system('cls')

numeros = [[22,33,34],[66,77],[12,11,13,15]]
impnum = []

for i in numeros:
    for y in i:
        if y%2 == 1:
            impnum.append(y)


for i in impnum:
    print(i)