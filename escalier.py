import turtle
t = turtle.Turtle()

def stairs(length, nb):
    for i in range(nb):
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.right(90)

    t.forward(30)

stairs(30, 8)

turtle.done()