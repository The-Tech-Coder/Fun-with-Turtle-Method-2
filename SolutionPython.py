import turtle as t
from itertools import cycle

colors = cycle(["violet", "indigo", "blue", "green", "yellow", "orange", "red"])

def square(size, angle, shift):
    t.hideturtle()
    t.pencolor(next(colors))
    t.forward(size)
    t.left(90)
    t.forward(shift)
    square(size + 5, angle + 1, shift + 1)

t.bgcolor("black")
t.speed("fast")
t.pensize(10)
square(40, 0, 1)
