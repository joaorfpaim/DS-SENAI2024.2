import os
os.system('cls')

# numeros = []

# for i in range(3):
#     numeros.append(int(input(f'Digite o número {i+1}/3: ')))

# print(max(numeros))

num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior número.')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior número.')
elif num3 > num2 and num3 > num1:
    print(f'{num3} é o maior número.')
else:
    print('existem números iguais.')