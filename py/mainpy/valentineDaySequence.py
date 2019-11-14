# valentineDaySequence.py by Ayush

import time
import math
import turtle
turtle.Screen().title('visualization')

turtle.penup()
turtle.right(90)
turtle.forward(325)
turtle.pendown()
turtle.right(180)
n = input('n: ') # 2048
n = int(n)

x = 0
a = 0
z = 0
q = 3

while True:
    if n % 2 != 0:
        n *= 3
        n += 1
        turtle.color('red')

    else:
        n /= 2
        turtle.color('blue')

    time.sleep(.003)
    n = int(n)
    print(f'{x}. {n}')
    
    x += 1
    
    if z == 0:
        turtle.right(20)
        turtle.forward(n / q)
        a = 0

    if z == 1:
        turtle.left(20)
        turtle.forward(n / q)
        a = 1

    if n == 1 or n == -1:
        break

    if a == 0:
        z += 1

    if a == 1:
        z -= 1
