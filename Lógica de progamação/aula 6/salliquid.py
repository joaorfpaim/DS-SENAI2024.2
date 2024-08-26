salbruto = int(input('Digite seu salario bruto: '))
filhos = int(input('Digite quantos filhos você tem: '))
ir = salbruto*0.08
auxfam = filhos*(salbruto*0.02)

salliquido = salbruto-ir+auxfam

print(f'Seu sálario liquido é de R${salliquido:.2f}')