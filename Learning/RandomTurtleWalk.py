import turtle
import random
turtle = turtle.Turtle()
turtle.speed(10)
turtle.shape("turtle")

while 1 == 1:
    dir = random.choice(range(1, ))
    if dir == 1:
        turtle.forward(random.choice(range(10, 100)))
    else:
        turtle.back(random.choice(range(10, 100)))

    dis = random.choice(range(1,3))
    if dis == 1:
        turtle.left(random.choice(range(10, 361)))
    else:
        turtle.right(random.choice(range(10, 361)))