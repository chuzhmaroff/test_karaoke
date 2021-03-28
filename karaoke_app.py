import os
from tkinter import *
from tkinter import filedialog
import time

path_to_script = os.path.dirname(os.path.abspath(__file__))
path_to_lib_music = "{}/music_movie".format(path_to_script)

list_music_movie = []
for position in os.listdir(path_to_lib_music):
    list_music_movie.append(position)


def start_app():
    comp = str(choose_composition.get())
    console.insert(END, "Вы выбрали композицию - {}\n".format(comp))


def create_gui():
    frame_start_karaoke = Frame()
    win_1 = LabelFrame(text="Консоль информации")
    win_2 = LabelFrame(text="Список композиций")
    global console
    global text
    text = "Добро пожаловоть в приложение Караоке. \nВыберите композицию из списка ниже для старта\n"

    console = Text(win_1, width=100, height=7)
    console.insert(1.0, text)
    console.pack(side=LEFT)

    console_scroll = Scrollbar(win_1, command=console.yview)
    console_scroll.pack(side=LEFT, fill=Y)
    console.config(yscrollcommand=console_scroll.set)
    win_1.pack()

    # -
    global table_set_compositions
    table_set_compositions = OptionMenu(win_2, choose_composition, *list_music_movie)
    table_set_compositions.pack(side=BOTTOM)
    win_2.pack()

    buttom_start_karaoke = Button(frame_start_karaoke, text="Старт", command=start_app)
    buttom_start_karaoke.pack(side=RIGHT)
    frame_start_karaoke.pack(side=BOTTOM)


path_to_font = r"{}/roman.ttf".format(path_to_script)
font_for_window = ("Times New Roman", 9)
window = Tk()
window.title("Karaoke")
window.geometry('900x600+100+10')
window.resizable(0, 0)

choose_composition = StringVar(window)
choose_composition.set(list_music_movie[0])

create_gui()

frame = Frame()
frame.pack()

label = Label()
label.pack()

window.mainloop()
