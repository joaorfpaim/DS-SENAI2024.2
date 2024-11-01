import customtkinter as ctk

def media():
    n1 = float(und1.get())
    n2 = float(und2.get())
    n3 = float(und3.get())
    media = (n1 + n2 + n3)/3
    resultado.configure(text = f'A sua média foi de {media} pontos.')
    if media >= 6:
        resultado1.configure(text = 'Você foi aprovado.')
    else:
        resultado1.configure(text = 'Você foi reprovado.')
        
        

ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.maxsize(800,600)
janela.minsize(800,600)
janela.title('Media')


und1 = ctk.CTkEntry(janela,
                    placeholder_text= 'Digite a sua nota da 1° unidade',
                    width= 200,
                    height= 40)
und1.pack(pady = 10)

und2 = ctk.CTkEntry(janela,
                    placeholder_text= 'Digite a sua nota da 2° unidade',
                    width= 200,
                    height= 40)
und2.pack(pady = 10)

und3 = ctk.CTkEntry(janela, placeholder_text= 'Digite a sua nota da 3° unidade',
                    width= 200,
                    height= 40)
und3.pack(pady = 10)

botao = ctk.CTkButton(janela, text= 'calcular',
                      font= ('arial', 25, 'bold'),
                      fg_color= '#181922',
                      text_color= '#FFB6C1',
                      hover_color= '#4F4F4F',
                      command= media)
botao.pack(pady = 5)

resultado = ctk.CTkLabel(janela,
                         text= '',
                         font= ('arial', 18))
resultado.pack(pady = 5)

resultado1 = ctk.CTkLabel(janela,
                         text= '',
                         font= ('arial', 18))
resultado1.pack(pady = 5)

janela.mainloop()