numeros = []
for x in range(10):
    numeros.append(int(input('Digite 10 números inteiros:')))
    
media = sum(numeros)/len(numeros)

print(f'A média dos números é {media}')