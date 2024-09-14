import customtkinter as ctk
import os

#Funções
def shutdown():
    os.system('shutdown -s')
    
def restart():
    os.system('shutdown /r /t 0')
    
def logoff():
    os.system('shutdown -l')

#Interface
ctk.set_appearance_mode('dark')
janela = ctk.CTk('#181922')
janela.maxsize(400,300)
janela.minsize(400,300)
janela.title('Power Patch V 0.1')
janela.iconbitmap('bomb_19735.ico')

ctk.CTkLabel(janela, text= 'Power Patch', font= ('arial', 40, 'bold'), text_color= '#FFB6C1').pack(pady = 10)

desligar = ctk.CTkButton(janela, text= 'desligar', font= ('arial', 30, 'bold'), fg_color= '#FFB6C1', text_color= '#000000', hover_color= '#2A3B4C', width= 250, cursor= "hand2", command = shutdown) 
desligar.pack(pady = 5)

reiniciar = ctk.CTkButton(janela, text= 'reiniciar', font= ('arial', 30, 'bold'), fg_color= '#FFB6C1', text_color= '#000000', hover_color= '#2A3B4C', width= 250, cursor= "hand2", command = restart)
reiniciar.pack(pady = 5)

bloquear = ctk.CTkButton(janela, text= 'bloquear', font= ('arial', 30, 'bold'), fg_color= '#FFB6C1', text_color= '#000000', hover_color= '#2A3B4C', width= 250, cursor= "hand2", command = logoff)
bloquear.pack(pady = 5)


janela.mainloop()