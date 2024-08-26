import os
import time

os.system('cls')
numero = []
while True:
    n = int(input('Digite numeros que queira somar, quando quiser que a soma seja feita, digite 0: '))
    os.system('cls')
    
    if n == 0:
        time.sleep(3)
        break
    numero.append(n)
os.system('cls')
print(f'A soma dos números é {sum(numero)}')
time.sleep(10)
os.system('cls')
