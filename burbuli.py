from random import *
from tkinter import *
from math import *

#mērķis ir uztaisīt programmu, kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti

window = Tk()
window_width = 1280
window_height = 720
window.title("Burbuļu spridzinātājs")

canvas = Canvas(window, width=window_width, height=window_height, bg="#38d5e0")
canvas.pack()
kuga_id = canvas.create_oval(10, 10, 80, 40, outline="black", width=5)

while True:
    window.update()

mainloop()