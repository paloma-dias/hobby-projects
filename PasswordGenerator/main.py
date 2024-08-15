from email import message
from msilib.schema import CheckBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import string 
import random

# Cores
cor0 = '#444466' # azul petróleo
cor1 = '#feffff' # branco
cor2 = '#f05a43' # alaranjado

# Janelas
janela = Tk()
janela.title('')
janela.geometry('295x356')
janela.configure(bg=cor1)

# Frame Cima
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

# Frame Baixo
frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')  
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Estilo
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Imagem
#img = Image.open('password.png')
#img = img.resize((30, 30), Image.ANTIALIAS)
#img = ImageTk.PhotoImage(img)

# Label Logo
label_logo = Label(frame_cima, height=60, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
label_logo.place(x=2, y=0)

# Label Título
label_title = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor1, fg=cor0)
label_title.place(x=35, y=4)

# Label Linha
label_linha = Label(frame_cima, text='', width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor2, fg=cor0)
label_linha.place(x=0, y=35)

# Função Gerar Senha
def criar_senha(): 
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()*;/,_-'

    global combinar

    # Condição para maiúscula
    if estado_1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
        pass

    # Condição para minúscula
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

    # Condição para números
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # Condição para símbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))
    
    label_senha['text'] = senha

    # Função Copiar Senha
    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'A senha foi copiada com sucesso!')

    # Botão Copiar Senha
    btn_copiar_senha = Button(frame_baixo, command=copiar_senha, text='Copiar', width=7, height=2, relief='raised', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
    btn_copiar_senha.grid(row=0, column=1, columnspan=1, sticky=NW, padx=5, pady=10)

# Label Senha
label_senha = Label(frame_baixo, text='- - - - - -', width=21, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=cor1, fg=cor0)
label_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

# Label Caracteres
label_info = Label(frame_baixo, text='Número total de caracteres na senha', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
label_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

# SpinBox
var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

# Variaveis
alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()*;/,_-'

# Frame Caracteres
frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor1, pady=0, padx=0, relief='flat')  
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# Estado, Check, Label -> 1
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
label_check_1 = Label(frame_caracteres, text='ABC Letras maiúsculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
label_check_1.grid(row=0, column=1, sticky=NW, padx=2, pady=7)

# Estado, Check, Label -> 2
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
label_check_2 = Label(frame_caracteres, text='ABC Letras minúsculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
label_check_2.grid(row=1, column=1, sticky=NW, padx=2, pady=7)

# Estado, Check, Label -> 3
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
label_check_3 = Label(frame_caracteres, text='123 Números', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
label_check_3.grid(row=2, column=1, sticky=NW, padx=2, pady=7)

# Estado, Check, Label -> 4
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=cor1)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
label_check_4 = Label(frame_caracteres, text='Símbolos', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
label_check_4.grid(row=3, column=1, sticky=NW, padx=2, pady=7)

# Botão Gerar Senha
btn_gerar_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha', width=33, height=1, relief='flat', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
btn_gerar_senha.grid(row=5, column=0, columnspan=5, sticky=NSEW, padx=10, pady=2)

janela.mainloop()
