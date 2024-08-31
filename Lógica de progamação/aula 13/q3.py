import os 
os.system('cls')

def calcula_sal(salario):
    if salario <= 280:
        sal = salario*0.2 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 20% e aumento de {salario*0.2:.2f}')
    elif salario >= 280 and salario <= 700:
        sal = salario*0.15 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 15% e aumento de {salario*0.15:.2f}')
    elif salario >= 700 and salario <= 1500:
        sal = salario*0.10 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 10% e aumento de {salario*0.10:.2f}')
    elif salario <= 1500:
        sal = salario*0.5 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 5% e aumento de {salario*0.5:.2f}')

salario = float(input('Digite seu salario, para que possa ser reajustado: '))

calcula_sal(salario)

"""
import os 
os.system('cls')

def calcula_sal(salario):
    if salario <= 280:
        sal = salario*0.2 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 20% e aumento de {salario*0.2:.2f}')
    elif salario >= 280 and salario <= 700:
        sal = salario*0.15 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 15% e aumento de {salario*0.15:.2f}')
    elif salario >= 700 and salario <= 1500:
        sal = salario*0.10 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 10% e aumento de {salario*0.10:.2f}')
    elif salario <= 1500:
        sal = salario*0.5 + salario
        print(f'O seu salário era de {salario:.2f}R$ e foi para {sal:.2f}, com um percentual de aumento de 5% e aumento de {salario*0.5:.2f}')

salario = float(input('Digite seu salario, para que possa ser reajustado: '))
calcula_sal(salario)
"""   
    
