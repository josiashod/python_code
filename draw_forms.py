import turtle
t = turtle.Turtle()

def stairs(length, nb):
    for i in range(nb):
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.right(90)

    t.forward(30)

def scare(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def scares(length, nb):
    for i in range(1, nb):
        new_length = i * length 
        scare(new_length)

scares(10, 100)
# scare(100)

turtle.done()