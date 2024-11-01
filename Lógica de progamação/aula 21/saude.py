import customtkinter as ctk

#Função

def calculo(event=None):
    altura = float(a.get())
    peso = int(p.get())
    imc = peso/(altura**2)
    if imc < 18.5:
        resultado.configure(text = f'{nome.get()}, você está com magreza.')
    elif imc >= 18.5 and imc < 25:
        resultado.configure(text = f'{nome.get()}, você está com peso ideal.')
    elif imc >= 25 and imc < 30:
        resultado.configure(text = f'{nome.get()}, você está com sobrepeso.')
    elif imc >= 30 and imc < 25:
        resultado.configure(text = f'{nome.get()}, você está com obesidade.')
    
def limpar():
    nome.delete(0,'end')
    p.delete(0,'end')
    a.delete(0,'end')
    resultado.configure(text = '')


#Interface
ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.maxsize(500,500)
janela.minsize(500,500)
janela.title('Saúde')


ctk.CTkLabel(janela,
             text= 'Saúde',
             font= ('arial', 40, 'bold'),
             text_color= '#FFB6C1').pack(pady = 10)

nome = ctk.CTkEntry(janela,
                    placeholder_text= 'Nome',
                    width= 200,
                    height= 40
)
nome.pack(pady = 5)

p = ctk.CTkEntry(janela,
                    placeholder_text= 'Peso (Kg)',
                    width= 200,
                    height= 40)
p.pack(pady = 5)

a = ctk.CTkEntry(janela,
                    placeholder_text= 'Altura (cm)',
                    width= 200,
                    height= 40)
a.pack(pady = 5)


calcular = ctk.CTkButton(janela,
                         text= 'calcular',
                         width= 95,
                         height= 40,
                         command = calculo)
calcular.place(y = 223, 
               x = 152)
limpar = ctk.CTkButton(janela,
                         text= 'limpar',
                         width= 95,
                         height= 40,
                         command = limpar)
limpar.place(y = 223,
             x = 252)


resultado = ctk.CTkLabel(janela, text= '', font= ('arial', 18))
resultado.pack(pady = 60)

janela.bind('<Return>', calculo)
janela.mainloop()
