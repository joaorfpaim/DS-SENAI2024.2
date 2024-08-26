salario = int(input('Digite o seu salario: '))
if (salario < 2000):
    ir = 0
elif (salario >= 2000 and salario < 3500):
    ir = salario*0.08
elif (salario >= 3500 and salario < 10000):
    ir = salario*0.12
else:
    ir = salario*0.20
print(f'O valor do seu imposto de renda é R${ir:.2f}')