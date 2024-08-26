nome = input('Qual o nome do senhor?: ')
distancia = int(input('Qual é a distancia a ser percorrida (km/h)?: '))
consumo = int(input('Qual consumo médio do seu carro (km/l)?: '))
combustivel = float(input('Qual o preço do combustivel na sua região?: '))

preco = (distancia/consumo)*combustivel 
print(f'{nome}, o senhor ira gastar R${preco:.2f} na sua viagem.')
