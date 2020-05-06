# ССЗДАНИЕ ОКНА
from tkinter import *

window = Tk()
window.title('Snake')

c = Canvas(window, width=1000, height=1000, bg='#404040')
c.pack()
window.mainloop()

# СОЗДАНИЕ ЗМЕЙКИ
n = 10
m = 10


class Class(object):
    def __init__(self, x, y):
        self.obg = c.create_rectangle(x, y, x + n, y + m, fill='white')


class Snake(object):
    def __init__(self, elements):
        self.elements = elements
        self.drive = {'Down': (0, 1),
                      'Up': (0, -1),
                      'Right': (1, 0),
                      'Left': (-1, 0), }
        self.begin = self.drive['Right']

    def move(self):
        for i in range(len(self.elements) - 1):
            element = self.elements[i].obg
            x1, y1, x2, y2 = c.coords(self.elements[i + 1].obg)
            c.coords(element, x1, y1, x2, y2)
        x1, y1, x2, y2 = c.coords(self.elements[-2].obg)
        c.coords(self.elements[-1].obg,
                 x1 + self.begin[0] * n,
                 x1 + self.begin[0] * m,
                 x1 + self.begin[0] * n,
                 x1 + self.begin[0] * m)

    def dist(self, dist):
        if self.dist in self.drive:
            self.begin = self.drive[self.dist]

    def add(self):
        last_el = c.coords(self.elements[0].obg)
        x = last_el[2] - n
        y = last_el[3] - m
        self.elements.obg(0, Class(x, y))


# СОЗДАЁМ ЭЛЕМЕНТЫ
elements = [Class(n, m), Class(n * 2, m), Class(n * 3, m)]
