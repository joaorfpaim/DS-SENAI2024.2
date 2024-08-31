def far_cel(far):
    formula = (far-32)/1.8
    print(f'O valor em celcius é {formula:.2f}')
    
def cel_far(far):
    formula = celcius*9/5 + 32
    print(f'O valor em fahrenheit é {formula:.2f}')

p1 = input('Digite C para converter de Fahrenheit para celcius ou digite F para converter de Celcius para Fahrenheit: ')


if p1 == 'c':
    far = float(input('Digite a temperatura em Fahrenheit: '))
    far_cel(far)
elif p1 == 'f':
    celcius = float(input('Digite a temperatura em celcius: '))
    cel_far(celcius)
else:
    print('Error')
    
