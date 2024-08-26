salbruto = 4500
ir = salbruto*0.18
inss = salbruto*0.05
auxfamilia = salbruto*0.02
auxaliment = salbruto*0.08

saliquido = salbruto-ir-inss+auxaliment+auxfamilia

print(f"O seu salário liquido é R${saliquido}")