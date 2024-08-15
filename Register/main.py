from tkinter import *
from tkinter import ttk
import datetime as dt

lista_tipos = ['Galão', 'Caixa', 'Saco', 'Madeira']
lista_codigos = []

janela = Tk()

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%Y %H:%M') 
    codigo = len(lista_codigos)+1
    codigo_str = 'COD-{}'.format(codigo)
    lista_codigos.append((codigo, descricao, tipo, quant, data_criacao))

    print(lista_codigos)

janela.title('Ferramenta de cadastro de materiais')

label_descricao = Label(text='Descrição do Material')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unid = Label(text='Tipo da unidade do material')
label_tipo_unid.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quant = Label(text='Quantidade por unidade de material')
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quant = Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

btn_criar_codigo = Button(text='Criar Código', command=inserir_codigo)
btn_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)


janela.mainloop()