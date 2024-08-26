import os
os.system('cls')

def calcular_media(num1,num2,num3):
    media = (num1+num2+num3)/3
    return media

def resultado(m):
    if m >= 6:
        print(f'Você foi aprovado {m:.2f}.')
    else:
        print(f'Você foi reprovado {m:.2f}.')

num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
num3 = float(input('Digite terceira nota: '))

media = calcular_media(num1,num2,num3)

resultado(media)