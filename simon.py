order = [1, 2, 3, 2, 4]


def reader_and_cheker(xorder, yuserchose):
    for i in range(len(yuserchose)):
        if yuserchose[i] != xorder[i]:
            return(False)
    return(True)


from tkinter import *

mode = 'game'
user_chose = []


def on_buuton_1_krass_click():
    global user_chose
    if mode == 'initial':
        print("Ещё не время")
    else:
        user_chose.append(1)
    reader_and_cheker(order, user_chose)


def on_button_2_sely_click():
    global user_chose
    if mode == 'initial':
        print("Ещё не время")
    else:
        user_chose.append(2)
    reader_and_cheker(order, user_chose)


def on_button_3_sin_click():
    global user_chose
    if mode == 'initial':
        print("Ещё не время")
    else:
        user_chose.append(3)
    reader_and_cheker(order, user_chose)


def on_button_4_zolt_click():
    global user_chose
    if mode == 'initial':
        print("Ещё не время")
    else:
        user_chose.append(4)
    reader_and_cheker(order, user_chose)


def polerisovalka(x):
    root = Tk()
    root.geometry('600x580')
    root.title("Добро пожаловать в сИмон")
    root.resizable(False, False)
    fon = Frame(root, bg='#FDEAA8')
    simon = Label(root, fg='black', text='СимОн', font='Courier 80', bg='#FDEAA8')
    krasnaya_knopochka = Button(root, bg='#B00000', activebackground='#681C23', command=on_buuton_1_krass_click)
    krasnaya_knopochka.place(x=40, y=150, width=150, height=150)
    selyonaya_knopochka = Button(root, bg='#1b4a12', activebackground='#013220', command=on_button_2_sely_click)
    selyonaya_knopochka.place(x=240, y=350, width=150, height=150)
    sinyaya_knopochka = Button(root, bg='#003153', activebackground='#1A162A', command=on_button_3_sin_click)
    sinyaya_knopochka.place(x=240, y=150, width=150, height=150)
    zoltaya_knopochka = Button(root, bg='#E5BE01', activebackground='#B8860B', command=on_button_4_zolt_click)
    zoltaya_knopochka.place(x=40, y=350, width=150, height=150)
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    simon.place(x=40, y=20)
    oknosurovnem = Label(root, text='Уровень:', font='Courier 15', bg='#FDEAA9')
    oknosurovnem2 = Label(root, text=x, font='Courier 15', bg='#FDEAA9')
    oknosurovnem.place(x=440, y=150, height=40, width=95)
    oknosurovnem2.place(x=440, y=190, height=40, width=95)
    root.mainloop()


polerisovalka(1)
print(reader_and_cheker)