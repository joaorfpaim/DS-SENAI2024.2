temp = int(input('Qual é a temperatura autal?: '))
if temp > 15:
    print('Está frio.')
elif temp > 14 and temp < 26:
    print('Está agradável.')
else:
    print('Está quente.')
