from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()

# Проверяет запущено наше приложение или нет
app_running = True

size_canvas_x = 768
size_canvas_y = 768


# Событие на нажатие крестика в нашем приложении
def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Вы хотите выйти? "):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

tk.title("Игра крестики нолики")

""" Мы не можем менять размер экрана """
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y,
                bd=0, highlightthickness=0)
canvas.pack()
tk.update()


s_x = 3
s_y = 3
step_x = size_canvas_x
step_y = size_canvas_y


def draw_table():
    for i in range(0, s_x):
        canvas.create_line(0, i, size_canvas_x, i)


    # Если приложение запущено то мы делаем обновление экрана
while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.005)
