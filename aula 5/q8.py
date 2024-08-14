numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
operacao = input('Digite uma das operações (+, -, x, /): ')

if operacao == '+':
    print(numero1 + numero2)
elif operacao ==  '-':
    print(numero1 - numero2)
elif operacao == 'x':
    print(numero1 * numero2)
elif operacao == '/':
    print(numero1 / numero2)
else:
    print('Operação inválida.')

        
