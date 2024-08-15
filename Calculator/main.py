from cProfile import label
from lib2to3.pgen2 import pgen
from tkinter import *
from tkinter import ttk

from numpy import pad

cor1 = '#222526' # preto
cor2 = '#ffffff' # braco
cor3 = '#356a96' # azul
cor4 = '#ded7d1' # cinza
cor5 = '#e38436' # laranja

#Janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('280x340')
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width=280, height=80, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_quadro = Frame(janela, width=280, height=400)
frame_quadro.grid(row=1, column=0)

#Variaveis
todos_valores = ''
valor_texto = StringVar()

#Função guardar str e exibir
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    #Exibir Valor
    valor_texto.set(todos_valores)

#Função Calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    #Exibir Resultado
    valor_texto.set(resultado)

#Função Limpar Tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#Label
app_label = Label(frame_tela, textvariable=valor_texto, width=18, height=3, padx=10, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2).place(x=0, y=0)

#Botões
bnt1 = Button(frame_quadro, command=limpar_tela, text='C', width=13, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=0)
bnt2 = Button(frame_quadro, command = lambda: entrar_valores('%'), text='%', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=140, y=0)
bnt3 = Button(frame_quadro, command = lambda: entrar_valores('/'),text='/', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=210, y=0)


bnt4 = Button(frame_quadro, command = lambda: entrar_valores('7'), text='7', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=52)
bnt5 = Button(frame_quadro, command = lambda: entrar_valores('8'), text='8', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=70, y=52)
bnt6 = Button(frame_quadro, command = lambda: entrar_valores('9'), text='9', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=140, y=52)
bnt7 = Button(frame_quadro, command = lambda: entrar_valores('*'), text='*', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=210, y=52)


bnt8 = Button(frame_quadro, command = lambda: entrar_valores('4'), text='4', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=104)
bnt9 = Button(frame_quadro, command = lambda: entrar_valores('5'), text='5', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=70, y=104)
bnt10 = Button(frame_quadro, command = lambda: entrar_valores('6'), text='6', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=140, y=104)
bnt11 = Button(frame_quadro, command = lambda: entrar_valores('-'), text='-', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=210, y=104)


bnt12 = Button(frame_quadro, command = lambda: entrar_valores('1'), text='1', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=156)
bnt13 = Button(frame_quadro, command = lambda: entrar_valores('2'), text='2', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=70, y=156)
bnt14 = Button(frame_quadro, command = lambda: entrar_valores('3'), text='3', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=140, y=156)
bnt15 = Button(frame_quadro, command = lambda: entrar_valores('+'), text='+', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=210, y=156)


bnt16 = Button(frame_quadro, command = lambda: entrar_valores('0'), text='0', width=13, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=208)
bnt17 = Button(frame_quadro, command = lambda: entrar_valores('.'), text='.', width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=140, y=208)
bnt18 = Button(frame_quadro, command= calcular, text='=', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=210, y=208)


janela.mainloop()