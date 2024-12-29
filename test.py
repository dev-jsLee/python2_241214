import tkinter as tk
from turtle import TurtleScreen, RawTurtle
import random


BASE_X = -234
BASE_Y = -210
OFFSET_X = 2


class Bar(RawTurtle):
    def __init__(self, _canvas, _size):
        super().__init__(_canvas)
        self.size = _size
        self.color_code = f"#{5 * _size:02x}{200 - 5 * _size:02x}{5 * _size:02x}"
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.turtlesize(1 + 0.2 * _size, 0.5)
        self.color(self.color_code)

    def set_position(self, position):
        self.goto(BASE_X + (OFFSET_X + 10) * position, BASE_Y + 2 * self.size)
        self.showturtle()

def randomize():
    random.shuffle(arr)
    for i in range(40):
        bar[arr[i]].set_position(i)


root = tk.Tk()
root.title("졍렬 알고리즘 시각화")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

screen = TurtleScreen(canvas)

arr = list(range(40))
bar = []
screen.tracer(0)
for i in range(40):
    bar.append(Bar(screen, i))
    bar[i].set_position(i)
screen.tracer(1)

screen.ontimer(randomize, 1000)

root.mainloop()
