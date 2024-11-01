import customtkinter as ctk

def calculo(event = None):
    vel = int(velocidade.get())

    if vel > 80 and vel < 300:
        vel = vel - 80
        resultado.configure(text = f'Você foi multado em {vel*5}R$')
    elif vel > 299:
        resultado.configure(text = 'Erro')
        
    else:
        resultado.configure(text = 'Você não foi multado.')

ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.maxsize(500,500)
janela.minsize(500,500)
janela.title('Velocidade')


ctk.CTkLabel(janela,
             text= 'Velocidade',
             font= ('arial', 40, 'bold'),
             text_color= '#FFB6C1').pack(pady = 10)

velocidade = ctk.CTkEntry(janela,
                    placeholder_text= 'Digite a velocidade do carro(KM)',
                    width= 200,
                    height= 40)
velocidade.pack(pady = 10)

multa = ctk.CTkButton(janela,
                       text= 'calcular multa',
                       font= ('arial', 10, 'bold'),
                       fg_color= '#FFB6C1',
                       text_color= '#000000',
                       hover_color= '#2A3B4C',
                       width= 100,
                       cursor= "hand2",
                       command= calculo) 
multa.pack(pady = 5)

resultado = ctk.CTkLabel(janela,
                         text= '',
                         font= ('arial', 18, 'bold'))
resultado.pack(pady = 5)     

janela.bind('<Return>', calculo)
janela.mainloop()