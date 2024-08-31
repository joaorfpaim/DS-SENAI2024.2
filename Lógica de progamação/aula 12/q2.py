import os 
os.system('cls')

vogais = ['a','e','i','o','u','ã''A','E','I','O','U','Ã']
texto = input('Digite uma palavra: ')


def vog(texto):
    cont = 0
    for i in texto:
        if i in vogais:
            cont += 1
    print(f'A quantidade de vogais é {cont}')
        
vog(texto)
