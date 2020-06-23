from tkinter import *

import time

root = Tk()

level = 1
mode = 'initial'
user_chose = []
result = 0
r = 3


def begin():
    root.geometry('600x580')
    root.title("Добро пожаловать в симОн")
    root.resizable(False, False)
    fon = Frame(root, bg='#FDEAA8')
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    simon = Label(root, fg="black", bg='#FDEAA8', text="Добро пожаловать в СимОн!", font="Serif 25")
    simon.place(x="45", y="80")
    description = Label(root, fg="black", bg='#FDEAA8', text="Что надо делать? Всё просто!\nПодождите пока СимОн покажет\nвам последовательность кнопок\n(они будут выделяться цветом)\nи повторите её нажимая на кнопки.\nЧем выше уровень тем больше кнопок.\nУдачи Дружок", font='Serif 16', justify="left")
    description.place(x='45', y="200")
    but_begin = Button(root, bg="#B00000", activebackground='#681C23', text="Начать", font='Courier', fg="white", command=passsf)
    but_begin.place(x="230", y="450")


def movecreator(r):
    import random
    global order
    order = random.choices([1, 2, 3, 4], k=r)

def passsf():
    global mode
    global user_chose
    polerisovalka(level)
    movecreator(r)
    user_chose = []
    root.after(500, show_order)
    mode = "game"




def continue_game():
    global level
    global r
    global mode
    root.geometry('600x580')
    root.title("Добро пожаловать в симОн")
    root.resizable(False, False)
    fon = Frame(root, bg='#FDEAA8')
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    simon = Label(root, fg="black", bg='#FDEAA8', text="МЫЛЫДЕЦ!!!", font="Serif 50")
    simon.place(x="45", y="100")
    but_cont = Button(root, bg="#B00000", activebackground='#681C23', text="Следующий уровень", font='Serif', fg="white", command=passsf)
    but_cont.place(x="170", y="400")
    r += 1
    level += 1
    mode = 'initial'


def game_over():
    global level
    global r
    global mode
    root.geometry('600x580')
    root.title("Добро пожаловать в симОн")
    root.resizable(False, False)
    fon = Frame(root, bg='#FDEAA8')
    simon = Label(root, fg="black", bg='#FDEAA8', text="GAME OVER...", font="Serif 50")
    but_begin = Button(root, bg="#B00000", activebackground='#681C23', text="Начать с начала", font='Serif', fg="white", command=passsf)
    simon.place(x="45", y="100")
    but_begin.place(x="170", y="400")
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    level = 1
    r = 3
    mode = 'initial'



def reader_and_cheker(xorder, yuserchose):
    # print(yuserchose)
    for i in range(len(yuserchose)):
        if yuserchose[i] != xorder[i]:
            return False
    if len(yuserchose) == len(xorder):   # Любое число совподающие с последним будет вызывать эту функцию
        continue_game()
    return True


def on_button_click(x):
    global result
    global user_chose
    if mode == 'initial':
        pass
    else:
        user_chose.append(x)
    result = reader_and_cheker(order, user_chose)
    if result == False:
        game_over()



def on_buuton_1_krass_click():
    on_button_click(1)



def on_button_2_sely_click():
    on_button_click(2)



def on_button_3_sin_click():
    on_button_click(3)



def on_button_4_zolt_click():
    on_button_click(4)



def polerisovalka(x):
    global krasnaya_knopochka
    global selyonaya_knopochka
    global sinyaya_knopochka
    global zoltaya_knopochka
    root.geometry('600x580')
    root.title("Добро пожаловать в симОн")
    root.resizable(False, False)
    fon = Frame(root, bg='#FDEAA8')
    simon = Label(root, fg='black', text='СимОн', font='Serif 80', bg='#FDEAA8')
    krasnaya_knopochka = Button(root, bg='#B00000', bd="6", activebackground='#681C23', command=on_buuton_1_krass_click)
    krasnaya_knopochka.place(x=40, y=150, width=150, height=150)
    selyonaya_knopochka = Button(root, bg='#1b4a12', bd="6", activebackground='#013220', command=on_button_2_sely_click)
    selyonaya_knopochka.place(x=240, y=350, width=150, height=150)
    sinyaya_knopochka = Button(root, bg='#003153', bd="6", activebackground='#1A162A', command=on_button_3_sin_click)
    sinyaya_knopochka.place(x=240, y=150, width=150, height=150)
    zoltaya_knopochka = Button(root, bg='#E5BE01', bd="6", activebackground='#B8860B', command=on_button_4_zolt_click)
    zoltaya_knopochka.place(x=40, y=350, width=150, height=150)
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    simon.place(x=40, y=20)
    oknosurovnem = Label(root, text='Уровень:', font='Serf 15', bg='#FDEAA9')
    oknosurovnem2 = Label(root, text=x, font='Serif 15', bg='#FDEAA9')
    oknosurovnem.place(x=440, y=150, height=40, width=95)
    oknosurovnem2.place(x=440, y=190, height=40, width=95)


def set_normal_colors():
    global krasnaya_knopochka
    global selyonaya_knopochka
    global sinyaya_knopochka
    global zoltaya_knopochka
    krasnaya_knopochka['bg'] = '#B00000'
    selyonaya_knopochka['bg'] = '#1b4a12'
    sinyaya_knopochka['bg'] = '#003153'
    zoltaya_knopochka['bg'] = '#E5BE01'


def show_order():
    global order
    global krasnaya_knopochka
    global selyonaya_knopochka
    global sinyaya_knopochka
    global zoltaya_knopochka
    for i in order:
        # print(i)
        if i == 1:
            krasnaya_knopochka['bg'] = '#681C23'
        if i == 2:
            selyonaya_knopochka['bg'] = '#013220'
        if i == 3:
            sinyaya_knopochka['bg'] = '#1A162A'
        if i == 4:
            zoltaya_knopochka['bg'] = '#B8860B'
        root.update()
        time.sleep(0.6)
        set_normal_colors()
        root.update()
        time.sleep(0.3)


def main():
   begin()


main()



root.mainloop()