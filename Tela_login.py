from multiprocessing.connection import Client
from tkinter import *
import customtkinter
from tkinter import messagebox
import dba
# Tela de Cadastro de funcionarios 
class Tela_Principal():
    
    # Atributos que classe Tela Funcionarios
    def __init__(self,usuario):
        self.tela = customtkinter.CTk()
        self.P_tema()
        self.usuario = usuario
        self.P_config()
        self.Tela_Fun()
        self.tela.mainloop()
    # Define o tema da tela funcionarios
    def P_tema(self):
        customtkinter.set_appearance_mode('Dark')
        customtkinter.set_default_color_theme('dark-blue')
    
    # Define as configurações da tela fun
    def P_config(self):
        self.tela.geometry('1000x600')
        self.tela.title(self.usuario)
        self.tela.iconbitmap('icon.ico')
        self.tela.resizable(False,False)
    
    
    def Tela_Fun(self):
        #Trabalhando com a imagem 
        img_fundo = PhotoImage(file='Fundoalt.png')
        img_fu = customtkinter.CTkLabel(master=self.tela,image=img_fundo,text=None)
        img_fu.place(x=0,y=0)
        msg_top = customtkinter.CTkLabel(master=self.tela,text=f'Bem Vindo {self.usuario}',font=('Cooper',30))
        msg_top.place(x=400,y=10)
        Menu_frame = customtkinter.CTkFrame(master=self.tela, width=510, height=430,fg_color='Black', border_width=2) 
        Menu_frame.place(x=245,y=70)
        
        bt_sair = customtkinter.CTkButton(master=Menu_frame,width=500,height=100,text='Sair',font=('Segoe Print',20),text_color='Black',fg_color='White',hover_color='Green',command=lambda:quit())
        bt_sair.place(x=5,y=150)
        
        


#Tela_Principal('Teste')
root = customtkinter.CTk()


# Criando a classe tela de login
class Tela_login():
    def __init__(self):
        # Atributos que classe  Login/Cadastro
        self.Tema()
        self.Config()
        self.Tela_label()
        self.root = root
        root.mainloop()
   

    # Tema da tela
    def Tema(self):
        customtkinter.set_appearance_mode('Dark')
        customtkinter.set_default_color_theme('dark-blue')
    
    # Conifg da tela
    def Config(self):
        root.title('Login')
        root.geometry('810x400')
        root.resizable(False,False)
        # root.iconbitmap('icon.ico')       

    def Tela_label(self):
        # Trabalhando com as imagens 
        img = PhotoImage(file='Imagee.png')
        imgver = PhotoImage(file='Senhaico.png')
        label1 = customtkinter.CTkLabel(master=root, image=img, text=None)
        label1.pack(side='left')
        imagem = PhotoImage(file='Top.png')


        # Criando o Frame da tela de login
        frame = customtkinter.CTkFrame(master=root, width=380,height=400,border_width=2,fg_color='Black')
        frame.pack(side='left')
        label1 = customtkinter.CTkLabel(master=frame, image=imagem,text=None)
        label1.place(x=10, y=0)
        label1 = customtkinter.CTkLabel(master=frame, text='Usuário:', font=('Constantia',20))
        label1.place(x=5, y=120)
        usuario = customtkinter.CTkEntry(master=frame, placeholder_text='Nome de usuário', width=170, height=30)
        if len(dba.Banco_Dados().Pegar_Ultimo()) > 0:
            usuario.insert(0,dba.Banco_Dados().Pegar_Ultimo()[0][1])
        usuario.place(x=80, y=120)
        label1 = customtkinter.CTkLabel(master=frame, text='Senha:', font=('Constantia',20))
        label1.place(x=5,y=160)
        # Função de mudar o tema da tela de login 
        def Mudar_tema(escolha):
            customtkinter.set_appearance_mode(escolha)
            if escolha == 'System':
                frame.configure(fg_color='silver')
            else:
                frame.configure(fg_color='Black')


        #Menu de Opções
        menu_tema = customtkinter.CTkOptionMenu(master=frame,values=['Dark','System'],button_hover_color='Green',command=Mudar_tema)
        menu_tema.place(x=5,y=370)
        
        # Mostra a senha 
        def Troca(versenha):
            senha.configure(show='')
            versenha.pack_forget()
            versenha = customtkinter.CTkButton(master=frame,width=16,height=30,image=imgver,text=None,fg_color='Black',hover_color='Green',command=lambda:Des_Troca(versenha))
            versenha.place(x=250, y=160)
            
            def Des_Troca(versenha):
                senha.configure(show='*')
                versenha.pack_forget()
                versenha = customtkinter.CTkButton(master=frame,width=16,height=30,image=imgver,text=None,fg_color='Black',hover_color='Green',command=lambda:Troca(versenha))
                versenha.place(x=250, y=160)
        
        # Botão de ver senha
        versenha = customtkinter.CTkButton(master=frame,width=16,height=30,image=imgver,text=None,fg_color='Black',hover_color='Green',command=lambda:Troca(versenha))
        versenha.place(x=250, y=160)
        
        #Campo Digitar a senha 
        senha = customtkinter.CTkEntry(master=frame, placeholder_text='Senha',width=170, height=30,show='*')
        senha.place(x=80,y=160)
        
        # Criando um chekbox 
        chekbox = customtkinter.CTkCheckBox(master=frame, text='Salvar',command=lambda:dba.Banco_Dados().Salvar_Ultimo(usuario.get()),)
        chekbox.place(x=4,y=200)
        def recuperar_senha():
            import os
            account_sid = os.environ['AC7b9b67a5580a739c031c71385d41e39a']
            auth_token = os.environ['2f5dd1d68d0b64ed05b73fa95cb30ddb']
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     body="Teste ",
                     from_='+5571996696396',
                     to='+12525184710'
                 )

            print(message.sid)
        esqueceu_senha = customtkinter.CTkButton(master=frame,width=20,height=10,hover_color='Green',text='Forgot Password?',command=lambda:recuperar_senha())
        esqueceu_senha.place(x=5,y=305)
        
        # Exibir um mensagem na tela login
        def mensagem(usuario,senha):
            if usuario == '' or senha == '':
                msg = messagebox.showinfo(message='Preencha todos os campos')
                return
            lista = dba.Banco_Dados().Consultar(usuario)
            if len(lista) == 0: 
                msg = messagebox.showinfo(message='Usuário não cadastrado')
            elif usuario == lista[0][0] and senha == lista[0][1]:
                msg = messagebox.showinfo(message='Login realizado com sucesso')
                root.destroy()
                Tela_Principal(usuario)
            else:
                 msg = messagebox.showinfo(message='Usuário ou  Senha inválido')
        #Botão de Entrar 
        botao = customtkinter.CTkButton(master=frame, text='Entrar', width=100,height=40,hover_color='Green',command=lambda:mensagem(usuario.get(),senha.get()))
        botao.place(x=50,y=250)
        def Enter():
           mensagem(usuario.get(),senha.get())
        botao.bind('<Return>',lambda:Enter())
        def Tela_Cadastro():
            # Resetar as configurações do frame
            frame.pack_forget()
            root.title('Cadastro')
            
            # Criando a tela de cadastro , criando o Frame da tela de Cadastro
            frame_cadastro = customtkinter.CTkFrame(master=root, width=300, height=500)
            frame_cadastro.pack(side='right')
            Image_top = customtkinter.CTkLabel(master=frame_cadastro, image=imagem,text=None)
            Image_top.place(x=10, y=5)
            cad_usuario = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Nome de usuário', width=200, height=30)
            cad_usuario.place(x=50, y=100)
            cad_senha = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Senha', width=200,height=30,show='*')
            cad_senha.place(x=50, y=150)
            confi_senha  = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Confirmação da Senha', width=200, height=30,show='*')
            confi_senha.place(x=50, y=200)
            
            # Retorna para tela de Login 
            def Back():
                root.title('Login')
                frame_cadastro.pack_forget()
                frame.pack(side='right')
           
            # Botão da tela de cadastro
            Volta = customtkinter.CTkButton(master=frame_cadastro, text='Volta', width=70, height=40,hover_color='Green' ,command=lambda:Back())
            Volta.place(x=50, y=250)
            
            # Exibir um mensagem na tela cadastro
            def mensagem_box(usuario,senha,confisenha):
                verificador = dba.Banco_Dados().Consultar(usuario)
                if usuario == '' or senha == '':
                    msg = messagebox.showinfo(message='Preencha todos os campos')
                elif len(verificador) > 0:
                    msg = messagebox.showinfo(message='Usuário já cadastrado')    
                elif senha == confisenha:   
                    msg = messagebox.showinfo(message='Usuário salvo com sucesso')
                    dba.Banco_Dados().Cadastrar(usuario,senha)
                    Back()
                else:
                     msg = messagebox.showinfo(message='Erro: Senhas diferentes')
            # Botão de salvar O cadastro 
            cad_salva = customtkinter.CTkButton(master=frame_cadastro, text='Salvar', width=70, height=40,hover_color='Green' ,command=lambda:(mensagem_box(cad_usuario.get(),cad_senha.get(),confi_senha.get())))
            cad_salva.place(x=150, y=250)
        # Botao para ir a tela de cadastro
        cadastro = customtkinter.CTkButton(master= frame, text='Cadastro',hover_color='Green', width=100, height=40,command=Tela_Cadastro)
        cadastro.place(x=160, y=250)

Tela_login()
