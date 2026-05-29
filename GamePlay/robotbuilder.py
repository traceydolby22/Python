import turtle as t

def rectangle(horizontal, vertical, color) : 
    t.pendown()
    t.pencolor(color)
    t.pensize(5)
    t.fillcolor(color)
    t.begin_fill()
    for counter in range(1, 3) :
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed("slow")
t.bgcolor("DodgerBlue")

#feet 
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

#legs
t.goto(-25, -50)
rectangle(15, 100, 'powderblue')
t.goto(-55, -50)
rectangle(15, 100, 'powderblue')

#body
t.goto(-90, 100)
rectangle(100, 150, 'pink')

# arms
t.goto(-150, 70)
rectangle(60, 15, 'pink')
t.goto(-150, 110)
rectangle(15, 40, 'pink')

t.goto(10, 70)
rectangle(60, 15, 'pink')
t.goto(55, 110)
rectangle(15, 40, 'pink') 

#hands
t.goto(-155, 130)
rectangle(25, 25, 'peachpuff')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, 'peachpuff')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())

#neck
t.goto(-50, 120)
rectangle(15, 20, 'peachpuff')

#head
t.goto(-85, 170)
rectangle(80, 50, 'peachpuff')

#eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')

#mouth
t.goto(-65, 135)
rectangle(40, 5, 'green')

t.hideturtle()