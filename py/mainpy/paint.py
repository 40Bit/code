import turtle

x = turtle
screen = x.Screen()

def fwd():
    x.forward(20)

def bwd():
    x.backward(20)

def lft():
    x.left(20)

def rgt():
    x.right(20)

def clr():
    x.clear()

def upp():
    x.up()

def dwp():
    x.down()

def cln():
    turtle.clone()

def ooo():
    for x in range(0,30):
        x = turtle
        x.speed(100)
        x.circle(45)
        x.forward(1)
        x.speed(5)

def qwe():
    x.speed(100)
    x.forward(2000)
    x.backward(2000)
    x.speed(5)

x.Pen()
screen.title('paint.py')
screen.onkey(cln, "'")
screen.onkey(fwd, "Up")
screen.onkey(bwd, "Down")
screen.onkey(lft, "Left")
screen.onkey(rgt, "Right")
screen.onkey(clr, "/")
screen.onkey(upp, "(")
screen.onkey(dwp, ")")
screen.onkey(ooo, "!")
screen.onkey(qwe, "@")
screen.listen()

