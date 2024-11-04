import turtle
t = turtle.Turtle()
turtle.bgcolor("beige")

hlen = 225
hbre = 400
c1 = -(hbre), -(hlen)
c2 = -(hbre), hlen
c3 = hbre, hlen
c4 = hbre, -hlen
t.speed(5)
t.shape = "turtle"

t.color("#012169") # UK Navy
t.fillcolor("#012169")
t.begin_fill()
t.penup()
t.goto(c1)
t.pendown()
t.pensize(5)
t.goto(c2)
t.goto(c3)
t.goto(c4)
t.goto(c1)
t.end_fill()

t.color("white")
t.fillcolor("white")
t.begin_fill()
t.seth(90)
t.fd(25)
t.goto(330, 225)
t.goto(c3)
t.seth(270)
t.fd(25)
t.goto(-330, -225)
t.goto(c1)
t.seth(90)
t.fd(25)
t.end_fill()

t.penup()
t.goto(c4)
t.pendown()
t.begin_fill()
t.seth(90)
t.fd(25)
t.goto(-330, 225)
t.goto(c2)
t.seth(270)
t.fd(25)
t.goto(330, -225)
t.goto(c4)
t.seth(90)
t.fd(25)
t.end_fill()

t.penup()
t.fd(125)
hstripbc = t.pos()
t.pendown()
t.begin_fill()
t.seth(180)
t.fd(800)
t.seth(90)
t.fd(150)
t.seth(0)
t.fd(800)
t.seth(270)
t.fd(150)
t.end_fill()

t.penup()
t.goto(c2)
t.seth(0)
t.fd(325)
t.pendown()
t.begin_fill()
t.fd(150)
t.seth(270)
t.fd(450)
t.seth(180)
t.fd(150)
t.seth(90)
t.fd(450)
t.end_fill()

t.seth(0)
t.fd(37.5)
t.color("#C8102E") # Bright Red
t.fillcolor("#C8102E")
t.begin_fill()
t.fd(75)
t.seth(270)
t.fd(450)
t.seth(180)
t.fd(75)
t.seth(90)
t.fd(450)
t.end_fill()

t.penup()
t.goto(hstripbc)
t.seth(90)
t.fd(37.5)
t.pendown()
t.begin_fill()
t.fd(75)
t.seth(180)
t.fd(800)
t.seth(270)
t.fd(75)
t.seth(0)
t.fd(800)
t.end_fill()

for corner in [c1, c2, c3, c4]:
    x = 400
    y = 210
    tx = 145
    ty = 80
    if corner == c2 or corner == c1:
        x = -x
        tx = -tx

    if corner == c1 or corner == c4:
        y = -y
        ty = -ty

    t.penup()
    t.goto(corner)
    t.pendown()
    t.begin_fill()
    t.goto(tx, ty)
    if corner == c2 or corner == c1:
        t.seth(180)
    if corner == c3 or corner == c4:
        t.seth(0)
    t.fd(28)
    t.goto(x, y)
    t.goto(corner)
    t.end_fill()

turtle.done()