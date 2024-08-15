from mimetypes import init
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# Janela
janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

# Cores
cor1 = '#1C1C1C' # cinza - pesado
cor2 = '#363636' # cinza - leve
cor3 = '#ffffff' # branco
cor4 = '#fcc058' # laranja

# Frame
frame_top = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_top.grid(row=0, column=0)

frame_underside = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_underside.grid(row=1, column=0)

# Labels TOP
label_calend = Label(frame_top, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor1, fg=cor3).place(x=0, y=30)
label_idade = Label(frame_top, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor1, fg=cor4).place(x=0, y=70)

# Funcão calcular idade
def calcular():
    iniciar = calendario1.get()
    termino = calendario2.get()

    # Formatando os valores e atributos
    dia_iniciar, mes_iniciar, ano_iniciar = [int(f) for f in iniciar.split('/')]
    data_iniciar = date(ano_iniciar, mes_iniciar, dia_iniciar)

    dia_termino, mes_termino, ano_termino = [int(f) for f in termino.split('/')]
    data_nasc = date(ano_termino, mes_termino, dia_termino)


    anos = relativedelta(data_iniciar, data_nasc).years
    meses = relativedelta(data_iniciar, data_nasc).months
    dias = relativedelta(data_iniciar, data_nasc).days
    
    label_y["text"] = anos
    label_mm["text"] = meses
    label_dd["text"] = dias


# Labels UNDERSIDE / CALENDÁRIOS
label_dataInicial = Label(frame_underside, text="Data Inicial", height=1, padx=3, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor2, fg=cor3).place(x=30, y=30)
calendario1 = DateEntry(frame_underside, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/y', y=2022)
calendario1.place(x=190, y=30)

label_dataNasc = Label(frame_underside, text="Data de nascimento", height=1, padx=3, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor2, fg=cor3).place(x=30, y=60)
calendario2 = DateEntry(frame_underside, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/y', y=2022)
calendario2.place(x=190, y=60)

# Labels -> exibir resultado (y, mm, dd)
label_y = Label(frame_underside, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor2, fg=cor3)
label_y.place(x=60, y=135)
label_txtY = Label(frame_underside, text="anos", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 11'), bg=cor2, fg=cor3).place(x=60, y=175)

label_mm = Label(frame_underside, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor2, fg=cor3)
label_mm.place(x=140, y=135)
label_txtMM = Label(frame_underside, text="meses", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 11'), bg=cor2, fg=cor3).place(x=140, y=175)

label_dd = Label(frame_underside, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor2, fg=cor3)
label_dd.place(x=220, y=135)
label_txtDD = Label(frame_underside, text="dias", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 11'), bg=cor2, fg=cor3).place(x=220, y=175)

# Botão Calcular
btnCalc = Button(frame_underside, command=calcular, text="Calcular", height=1, width=20, relief='raised', overrelief='ridge', font=('Ivi 10 bold'), bg=cor4, fg=cor1).place(x=70, y=215)

janela.mainloop()

