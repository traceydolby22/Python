import turtle as t 
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

def draw_circle(size, angle, shift, shape) :
    t.pencolor(next(colors))
    next_shape = " "
    if shape == "circle" :
        t.circle(size)
        next_shape = "square"
    elif shape == "square" :
        for i in range(4) :
           t.forward(size *2)
           t.left(90)
        next_shape = "triangle" 
    elif shape == "triangle" :
        for i in range(3) :
            t.forward(size * 2)
            t.left(120)
        next_shape = "circle"
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle +1, shift + 1, next_shape)

t.bgcolor("black")
t.speed("slow")
t.pensize(2)
draw_circle(30, 0, 1,'circle')


