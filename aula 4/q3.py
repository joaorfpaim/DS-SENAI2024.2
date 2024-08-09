aluno = input('Nome completo: ')
und1 = int(input('Qual foi sua nota na primeira unidade?: '))
und2 = int(input('Qual foi sua nota na segunda unidade?: '))
und3 = int(input('Qual foi sua nota na terceira unidade?: '))
media = (und1+und2+und3)/3
print(f'{aluno}, sua media foi {media:.2f}')