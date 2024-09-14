import customtkinter as ctk

ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.geometry('500x500')

ctk.CTkLabel(janela, text = 'Login', font = ('arial', 28, 'bold'),text_color= '#FFB6C1').pack(pady = 10)

user = ctk.CTkEntry(janela, placeholder_text= 'Digite seu usuario', width= 200, height= 40)
user.pack(pady = 10)

senha = ctk.CTkEntry(janela, placeholder_text= 'Digite seu senha', width= 200, height= 40, show= '•')
senha.pack(pady = 10)

botao = ctk.CTkButton(janela, text= 'Entrar', font = ('arial', 25, 'bold'), fg_color= '#181922', text_color= '#FFB6C1', hover_color= '#4F4F4F')
botao.pack(pady = 5)

janela.mainloop()