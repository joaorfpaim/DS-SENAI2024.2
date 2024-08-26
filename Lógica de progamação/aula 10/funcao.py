#função
import os
import time

"""
num1 = int(input('Digite o primeiro número: ')) 
num2 = int(input('Digite o segundo número: ')) 
def soma(num1,num2):
    soma = num1 + num2
    print(f'A soma dos números é {soma}')
soma(num1,num2)
"""
"""

def texto():
    print('Oi seja bem vind!')
    
while True:
    entrada = int(input('Digite 1-Start, 2-Exit'))
    if entrada  == 1:
        texto()
    else:
        break
"""
os.system('cls')

def texto1():
    print('É par')
def texto2():
    print('É impar')

def verifica(num):
    if(num%2==0):
        texto1()
    else:
        texto2()

entrada = int(input('Digite um núnero: '))

verifica(entrada)
time.sleep(10)
os.system('cls')