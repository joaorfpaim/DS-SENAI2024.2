import os
import time

os.system('clear')
# Converte de celcius para Fahrenheit
def conversor1 (far):
    far = cel*9/5 + 32
    print(f'O valor em Fahrenheit é {far}')
# Converte de Fahrenheit para celcius
def conversor2 (cel):
    cel = (far - 32)/1.8
    print(f'O valor em celcius é {cel}')

    
p1 = input('Letra C converte para celcius, letra F converte para fahrenheit: ').lower()

if p1 == 'c':
    far = float(input('Digite os graus fahrenheit: '))
    conversor2(far)
elif p1 == 'f':
    cel = float(input('Digite os graus celcius: '))
    conversor1(cel)
else:
    print('Error')
    
time.sleep(10)
os.system('clear')