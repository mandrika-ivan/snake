
from tkinter import Tk, Canvas
import random

window = Tk()
window.title("Snake")


# ПЕРЕМЕННЫЕ
WIDTH = 1600
HEIGHT = 900
n = 50
game = True


#ОТДЕЛЬНЫЕ Ф-ЦИИ
def et():
    global eat
    lokx = n * random.randint(1, (WIDTH-n) / n)
    loky = n * random.randint(1, (HEIGHT-n) / n)
    eat = c.create_oval(lokx, loky, lokx+n, loky+n, fill="blue")


def main():
    global game
    if game:
        s.move()
        head = c.coords(s.elements[-1].obg)
        x1, y1, x2, y2 = head
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            game = False
        elif head == c.coords(eat):
            s.add()
            c.delete(eat)
            et()
        else:
            for i in range(len(s.elements)-1):
                if head == c.coords(s.elements[i].obg):
                    game = False
        window.after(100, main)
    else:
        state(r, 'normal')
        state(go, 'normal')

#КЛАСС ЭЛЕМЕНТОВ
class Class(object):
    def __init__(self, x, y):
        self.obg = c.create_rectangle(x, y, x+n, y+n, fill="white")

#КЛАСС ЗМЕИ
class Snake(object):
    def __init__(self, elements):
        self.elements = elements
        self.drive = {"Down": (0, 1), "Right": (1, 0), "Up": (0, -1), "Left": (-1, 0)}
        self.begin = self.drive["Right"]

    def move(self):
        for i in range(len(self.elements)-1):
            element = self.elements[i].obg
            x1, y1, x2, y2 = c.coords(self.elements[i+1].obg)
            c.coords(element, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.elements[-2].obg)
        c.coords(self.elements[-1].obg,
                 x1+self.begin[0]*n, y1+self.begin[1]*n,
                 x2+self.begin[0]*n, y2+self.begin[1]*n)

    def add(self):
        el = c.coords(self.elements[0].obg)
        x = el[2] - n
        y = el[3] - n
        self.elements.insert(0, Class(x, y))

    def dist(self, event):
        if event.keysym in self.drive:
            self.begin = self.drive[event.keysym]

    def s_new(self):
        for element in self.elements:
            c.delete(element.obg)

#ОТДЕЛЬНЫЕ Ф-ЦИИ
def state(st, state):
    c.itemconfigure(st, state=state)


def ff(event):
    global game
    s.s_new()
    game = True
    c.delete(eat)
    c.itemconfigure(r, state='hidden')
    c.itemconfigure(go, state='hidden')
    start()


def start():
    global s
    et()
    s = cr()
    c.bind("<KeyPress>", s.dist)
    main()


def cr():
    elements = [Class(n, n),
                Class(n*2, n),
                Class(n*3, n)]
    return Snake(elements)




#ХОЛСТ И ПАРАМЕТРЫ
c = Canvas(window, width=WIDTH, height=HEIGHT, bg="grey")
c.grid()
c.focus_set()
go = c.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER!", fill='red', state='hidden')
r = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3, fill='white', text="RESTART", state='hidden')
c.tag_bind(r, "<Button-1>", ff)
start()
window.mainloop()

