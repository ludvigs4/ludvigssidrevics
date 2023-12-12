from random import *
from tkinter import *

window = Tk()
window_width = 1280
window_height = 720

audekls = Canvas(window, width=window_width, height=window_height)
audekls.pack()

while True:
    color = choice(["darkblue", "darkgray", "gray"])
    x0 = randint(0, window_width)
    y0 = randint(0, window_height)
    d = randint(0, window_width/20)
    audekls.create_oval(x0, y0, x0+d, y0+d, fill=color)
    window.update()

mainloop()