import os
os.system('cls')

contador = 0


def contar(texto):
    global contador
    for i in texto:
        if i.isalpha():
            contador += 1
    return contador

texto = input('Digite uma palavra: ')

print(f'Sua palavra tem {contar(texto)} letra(s)')








"""
texto = []


def contador(texto):
    cont = 0
    texto.append(input('Digte uma palavra: '))
    for i in texto:
        cont = cont+1
        
        
contador(texto)
"""