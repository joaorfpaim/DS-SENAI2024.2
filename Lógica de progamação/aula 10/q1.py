notas = []

for i in range(3):
    notas.append(int(input(f'Digite a nota da {i+1}°und: ')))

def media(m):
    med = sum(notas)/len(notas)
    if med >= 6:
        print(f'Você foi aprova, sua média foi {med:.2f}')
    else:
        print('Você foi reprovado, sua média foi {med:.2f}')   
media(notas)