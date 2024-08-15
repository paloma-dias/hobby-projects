from tkinter import *
from tkinter import ttk, Text, messagebox
import datetime as dt
import tkinter
from tkinter.tix import ComboBox
from tkcalendar import Calendar, DateEntry
import pandas as pd


lista_generos = ['Romance', 'Ação', 'Comédia']
lista_livros = []

janela = Tk()
janela.title('Ficha de Leitura')

def inserir_livro():
    codigo = len(lista_livros)+1
    codigo_str = 'COD-{}'.format(codigo)
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    editora = entry_editora.get()
    genero = combobox_genero.get()
    quant_paginas = spin_paginas.get()
    data_publicacao = entry_data_publicacao.get()
    resumo = text_resumo.get()

    lista_livros.append((codigo, titulo, autor, editora, genero, quant_paginas, resumo, data_publicacao))
    messagebox.showinfo('Sucesso', 'Ficha inserida com sucesso. Informações')
    print(lista_livros)



label_titulo = Label(text='Título:')
label_titulo.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

entry_titulo = Entry()
entry_titulo.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=8)

label_autor = Label(text='Autor:')
label_autor.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

entry_autor = Entry()
entry_autor.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=8)

label_editora = Label(text='Editora:')
label_editora.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')

entry_editora = Entry()
entry_editora.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=8)

label_genero = Label(text='Gênero:')
label_genero.grid(row=4, column=0, padx=10, pady=10, sticky='nswe')

combobox_genero = ttk.Combobox(values=lista_generos)
combobox_genero.grid(row=4, column=1, padx=10, pady=10, columnspan=1)

label_quant_paginas = Label(text='Qtd pgs:')
label_quant_paginas.grid(row=4, column=3, padx=1, pady=10, sticky='nswe')

var = IntVar()
var.set(100)
spin_paginas = Spinbox(from_=0, to=1000, textvariable=var)
spin_paginas.grid(row=4, column=4, padx=10, pady=1, columnspan=2)

label_data_publicacao = Label(text='Data da publicação:')
label_data_publicacao.grid(row=5, column=0, padx=10, pady=10, sticky='nswe')

entry_data_publicacao = DateEntry(borderwidth=2, date_pattern='dd/mm/y')
entry_data_publicacao.grid(row=5, column=1, padx=10, pady=10, sticky='nswe')

label_resumo = Label(text='Resumo:')
label_resumo.grid(row=6, column=0, padx=10, pady=5, sticky='nswe')

text_resumo = Text(width=1, height=6)
text_resumo.grid(row=7, column=0, padx=10, pady=5, sticky='nswe', columnspan=8)

btn_inserir = Button(text='Inserir', command=inserir_livro)
btn_inserir.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=8)

janela.mainloop()