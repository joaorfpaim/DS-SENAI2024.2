"""
def remove_vogais(texto):
    vogais = 'aeiouAEIOU'
    palavra = ''
    for i in texto:
        if i not in vogais:
            palavra += i
    print(palavra)
    
texto = input('Digite uma palavra ou nome: ')

remove_vogais(texto)
"""
texto = []
def remove_vogais(texto):
    vogais = 'aeiouAEIOU'
    texto.append(input('Digite uma palavra ou nome: '))
    for i in texto:
        if i not in vogais:
            texto.remove(i)
    print(texto)
    

remove_vogais(texto)