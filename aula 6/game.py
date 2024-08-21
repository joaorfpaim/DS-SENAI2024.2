import os
import random
os.system('cls')

number = random.randint(0,100)

x = 1
while True:
    game = int(input('Digite um número entre 1 e 100: '))
    os.system('cls')
    x = x + 1
    if number == game:
        print(f'Parabéns, você acertou após {x} tentativas, o número certo é {number}')
        break
    elif number > game:
        print('Muito baixo')
    else:
        print('Muito alto')
