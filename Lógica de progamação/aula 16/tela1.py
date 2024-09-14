import customtkinter as ctk 
from tkinter import messagebox

def calcular(event=None):
    cdistancia = int(distancia.get())
    cconsumo = int(consumo.get())
    cpreco = float(preco.get())
    calculo = (cdistancia/cconsumo)*cpreco
    #messagebox.showinfo(calculo, f'O valor total para a viagem sera de R${calculo:.2f}')
    resultado.configure(text = f'O valor total para a viagem sera de R${calculo:.2f}')

ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.geometry('500x500')

ctk.CTkLabel(janela, text= 'Consumo de gasolina', font= ('arial', 40, 'bold'), text_color= '#FFB6C1').pack(pady = 10)

distancia = ctk.CTkEntry(janela, placeholder_text= 'Digite a distância', width= 200, height= 40)
distancia.pack(pady = 10)

consumo = ctk.CTkEntry(janela, placeholder_text= 'Digite o consumo por litro', width= 200, height= 40)
consumo.pack(pady = 10)

preco = ctk.CTkEntry(janela, placeholder_text= 'Digite o preço do combustivel', width= 200, height= 40)
preco.pack(pady = 10)

botao = ctk.CTkButton(janela, text= 'calcular', font= ('arial', 25, 'bold'), fg_color= '#181922', text_color= '#FFB6C1', hover_color= '#4F4F4F', command= calcular)
botao.pack(pady = 5)

resultado = ctk.CTkLabel(janela, text= '', font= ('arial', 18))
resultado.pack(pady = 5)


janela.bind('<Return>', calcular)
janela.mainloop()


