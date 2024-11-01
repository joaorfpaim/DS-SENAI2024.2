import os
os.system('cls')

num = int(input('Escolha um número: '))
op = input('Escolha um operador ')
# x = 0

# for i in range(10):
#     x = x+num
#     print(x)

for i in range(1,11):
    calculo = num + i
    print(f'{num} + {i} = {calculo}')