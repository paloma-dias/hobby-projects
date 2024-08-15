from pdb import post_mortem
import tkinter
from tkinter import *
from tkinter import ttk

import random

# Cores
c0 = "#444466"  # Preta
c1 = "#feffff"  # branca
c2 = "#6f9fbd"  # azul
c3 = "#38576b"  # valor
c4 = "#403d3d"   # letra
c5 = "#e06636"   # - profit
c6 = "#6dd695"   # + profit
c7 = "#ef5350"   # vermelha
c8 = "#00bfa5"   # + verde
c9 ="#fcfbf7"
cor_fundo = "#3b3b3b"

cor1='#f58b5d'
cor2='#ff333a'
cor3='#6bd66f'
cor4="#ab8918"

# Janela
janela = Tk()
janela.title('Jogo de Adivinhação')
janela.geometry('350x280')
janela.configure(bg=cor_fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

# Frames
frame_top = Frame(janela, width=350, height=30, bg=c1, pady=0, padx=0, relief='flat')
frame_top.grid(row=1, column=0, sticky=NW)

frame_body = Frame(janela, width=350, height=280, bg=cor_fundo, pady=0, padx=0, relief='flat')
frame_body.grid(row=2, column=0, sticky=NW)

# Estilo
style = ttk.Style(janela)
style.theme_use('clam')

# Label Frame Top
label_top = Label(frame_top, text='ADIVINHA O NÚMERO', anchor='center', font=('verdana 14 bold'), bg=c1, fg=c3)
label_top.place(x=55, y=0)

# Função Jogar
tentativas = 5
pontuacao = 0

# função para jogar e escolher números aleatórios
def jogar():

    # Labels Regras
    label_rule1['text'] = ''
    label_rule2['text'] = ''
    label_rule3['text'] = ''

    # gera números 8 aleatórios de 1 a 10
    numeros = random.sample(range(1,10),8)

    # escolhe um número aleatório
    resposta = random.choice(numeros)

    # função das tentativas e pontuações
    def estado_valor(v):
        numeros = random.sample(range(1,10),8)
        resposta = [random.choice(numeros)]

        global tentativas
        global pontuacao

        for i in resposta:

            # se acertar aumenta 2 tentativas e 10 pontos
            if v == i:
                tentativas += 2
                pontuacao += 10
                label_try['text'] = 'Tentativas: ' + str(tentativas)
                label_point['text'] = 'Pontuação: ' + str(pontuacao)

            # se errar reduz 1 tentativa
            else:
                tentativas -= 1
                label_try['text'] = 'Tentativas: ' + str(tentativas)

                # desabilitando os botões após acabar as tentativas
                if tentativas <= 0:
                    btn1['state'] = 'disable'
                    btn2['state'] = 'disable'
                    btn3['state'] = 'disable'
                    btn4['state'] = 'disable'
                    btn5['state'] = 'disable'
                    btn6['state'] = 'disable'
                    btn7['state'] = 'disable'
                    btn8['state'] = 'disable'

                    #apagando o texto dos botões
                    btn1['text'] = ''
                    btn2['text'] = ''
                    btn3['text'] = ''
                    btn4['text'] = ''
                    btn5['text'] = ''
                    btn6['text'] = ''
                    btn7['text'] = ''
                    btn8['text'] = ''
                    
                    # chamando a função gameover
                    game_over()
                
                else:
                    pass

    # botões para escolher um número
    btn1 = Button(frame_body, command=lambda:estado_valor(numeros[0]), text=numeros[0], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn1.place(x=40, y=70)
    btn2 = Button(frame_body, command=lambda:estado_valor(numeros[1]), text=numeros[1], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn2.place(x=108, y=70)
    btn3 = Button(frame_body, command=lambda:estado_valor(numeros[2]), text=numeros[2], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn3.place(x=176, y=70)
    btn4 = Button(frame_body, command=lambda:estado_valor(numeros[3]), text=numeros[3], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn4.place(x=244, y=70)
    btn5 = Button(frame_body, command=lambda:estado_valor(numeros[4]), text=numeros[4], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn5.place(x=40, y=133)
    btn6 = Button(frame_body, command=lambda:estado_valor(numeros[5]), text=numeros[5], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn6.place(x=108, y=133)
    btn7 = Button(frame_body, command=lambda:estado_valor(numeros[6]), text=numeros[6], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn7.place(x=176, y=133)
    btn8 = Button(frame_body, command=lambda:estado_valor(numeros[7]), text=numeros[7], width=5, height=2, font=('Ivi 15 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn8.place(x=244, y=133)

# função gameover
def game_over():
    global tentativas
    global pontuacao

    label_pointEnd = Label(frame_body, text='Pontuação final: ' + str(pontuacao), relief='raised', anchor='center', font=('ivi 15 bold'), bg=c1, fg=c2)
    label_pointEnd.place(x=52, y=90)

    label_game = Label(frame_body, text='GAME OVER', relief='raised', anchor='center', font=('ivi 15 bold'), bg=c1, fg=c2)
    label_game.place(x=52, y=130)

    tentativas = 5
    pontuacao = 0

    label_try['text'] = 'Tentativas: ' + str(tentativas)
    label_point['text'] = 'Pontuação: ' + str(pontuacao)

    # Botão Jogar novamente
    btn_play = Button(frame_body, command=jogar, text='Jogar Novamente', width=17, font=('Ivi 12 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
    btn_play.place(x=90, y=205)

# Label Frame Body

# Label Pontução
label_point = Label(frame_body, text='Pontuação: 0', anchor='center', font=('ivi 11 bold'), bg=cor_fundo, fg=c1)
label_point.place(x=40, y=30)

# Label Tentativas
label_try = Label(frame_body, text='Tentativas: 5', anchor='center', font=('ivi 11 bold'), bg=cor_fundo, fg=c1)
label_try.place(x=205, y=30)

# Label Linha Verde 'estilização'
label_line = Label(frame_body, text=' ', width=90, anchor='center', font=('Ivi 4'), bg=cor3, fg=c1)
label_line.place(x=39, y=59)

# Label Regras
label_rule1 = Label(frame_body, text='Tente adivinhar o número para pontuar', anchor='center', font=('Ivi 8 bold'), bg=cor_fundo, fg=c1)
label_rule1.place(x=40, y=80)

label_rule2 = Label(frame_body, text='Se acertar, ganha + 2 chances', anchor='center', font=('Ivi 8 bold'), bg=cor_fundo, fg=c1)
label_rule2.place(x=40, y=110)

label_rule3 = Label(frame_body, text='Se errar, reduz uma chance', anchor='center', font=('Ivi 8 bold'), bg=cor_fundo, fg=c1)
label_rule3.place(x=40, y=140)

# Botão Jogar
btn_play = Button(frame_body, command=jogar, text='Jogar', width=33, font=('Ivi 10 bold'), bg=c9, fg=c0, relief=RAISED, overrelief=RIDGE)
btn_play.place(x=40, y=170)

janela.mainloop()


