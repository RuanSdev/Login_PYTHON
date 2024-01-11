from tkinter import *
import customtkinter
from tkinter import messagebox
import dba
root = customtkinter.CTk()
class Tela_Fun():
    def __init__(self):
        self.Tema_Fun()
        self.Config_Fun()
        self.Tela_Funcionarios()
        self.root = root
        self.root.mainloop()
    def Tema_Fun(self):
        customtkinter.set_appearance_mode('white')
        customtkinter.set_default_color_theme('dark-blue')
    # Conifg da tela
    def Config_Fun(self):
        root.title('Login')
        root.geometry('1200x600')
        root.resizable(False,False)
        root.iconbitmap('icon.ico')
    def Tela_Funcionarios(self):
        frame = customtkinter.CTkFrame(master=root,width=500,height=1200,fg_color='#9CDAFF',border_width=2).pack(side='left')
