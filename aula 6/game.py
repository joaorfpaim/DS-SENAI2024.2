import os
import random
os.system('cls')

number = random.randint(0,100)

attempt = 0
while True:
    game = int(input('Digite um número entre 1 e 100: '))
    os.system('cls')
    attempt = attempt + 1
    if number == game:
        print(f'Parabéns, você acertou após {attempt} tentativas, o número certo é {number}')
        break
    elif number > game:
        print('Muito baixo')
    else:
        print('Muito alto')
