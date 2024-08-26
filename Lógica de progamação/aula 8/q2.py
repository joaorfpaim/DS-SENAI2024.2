numero = []
while True:
    n = int(input('Digite numeros que queira somar, quando quiser que a soma seja feita, digite zero: '))
    if n == 0:
        break
    numero.append(n)
print(f'A soma dos números é {sum(numero)}')