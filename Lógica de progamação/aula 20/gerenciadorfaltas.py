# João Ricardo, Gabriel Xavier

import customtkinter as ctk

# Funções

def calcular(event=None):
    carga = int(ch.get())
    fal = int(faltas.get())
    max_faltas = carga * 0.25
    faltas_restantes = max_faltas - (fal*4)
    porcentagens = (fal*4)/carga*100
    dias_restantes = faltas_restantes / 4
    resultado.configure(text = f'Você tem {porcentagens:.2f}% de faltas,\n você pode ainda ter {dias_restantes} dia(s) de falta')


# Interface

ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.maxsize(500,500)
janela.minsize(500,500)
janela.title('Gerenciador de faltas')


ctk.CTkLabel(janela,
             text= 'Gerenciador de Faltas',
             font= ('arial', 40, 'bold'),
             text_color= '#FFB6C1').pack(pady = 10)

ctk.CTkLabel(janela,
             text= 'Carga Horaria:',
             font= ('arial', 23, 'bold'),
             text_color= '#FFB6C1').place(x = 40, y = 90)

ch = ctk.CTkEntry(janela,
                placeholder_text= ' ',
                width= 200,
                height= 40)
ch.place(x = 205, y = 85)

ctk.CTkLabel(janela,
             text= 'Faltas (dia):',
             font= ('arial', 23, 'bold'),
             text_color= '#FFB6C1').place(x = 40, y = 140)

faltas = ctk.CTkEntry(janela,
                    placeholder_text= ' ',
                    width= 200,
                    height= 40)
faltas.place(x = 205, y = 135)

resultado = ctk.CTkLabel(janela, text= '', font= ('arial', 18))
resultado.place(x = 50, y = 200)

janela.bind('<Return>', calcular)
janela.mainloop()