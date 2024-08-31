import os
os.system('cls')

eleitores = int(input('Digite a quantidade de eleitores: '))




def votacao(eleitores):
    cand1 = 0
    cand2 = 0
    cand3 = 0
    for i in range(eleitores):

        votos = int(input('Escolha entre o candidato 1, 2 ou 3: '))
        if votos == 1:
            cand1 += 1
        elif votos == 2:
            cand2 += 1
        elif votos == 3:
            cand3 += 1
        else:
            print('Resposta incorreta.')
    print(f'O candidato 1 tem o total de {cand1} votos, o candidato 2 {cand2} votos e o candidato 3 {cand3} votos')
    
votacao(eleitores)