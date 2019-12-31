import turtle as x
import math as m

nums = [1, 0.5, 0.25, 0.125]
a = nums[0]
b = nums[1]
c = nums[2]
d = nums[3]
diam = 50
x.speed(200)


def diamond():
    global x, nums, a, b, c, d, diam
    
    #nums[0] = 1 # 1/1
    #nums[1] = 0.5 # 1/2
    #nums[2] = 0.25 # 1/4
    #nums[3] = 0.125 # 1/8
    y = 0
    l = 200

    alpha = [b, a, d, c]
    x.color("blue")

    x.penup()
    x.forward(l)
    x.pendown()
    x.left(90)
    x.forward(l)
    x.left(90)

    for i in range(0, 4):
        x.forward(l*2)
        x.left(90)
        x.write(alpha[y])
        y += 1

    if nums[0] > nums[1]:
        a = nums[0] - nums[1]

    elif nums[1] > nums[0]:
        a = nums[1] - nums[0]


    if nums[0] > nums[3]:
        b = nums[0] - nums[3]

    elif nums[3] > nums[0]:
        b = nums[3] - nums[0]


    if nums[1] > nums[2]:
        c = nums[1] - nums[2]

    elif nums[2] > nums[1]:
        c = nums[2] - nums[1]


    if nums[2] > nums[3]:
        d = nums[2] - nums[3]

    elif nums[3] > nums[2]:
        d = nums[2] - nums[3]

    for q in range(0, diam):
        nums[0] = a
        nums[1] = b
        nums[2] = c
        nums[3] = d

        x.forward(l)
        x.right(-45)
        
        j = (l*l) + (l*l)
        j = m.sqrt(j)
        l = j / 2

        if nums[0] > nums[1]:
            a = nums[0] - nums[1]

        elif nums[1] > nums[0]:
            a = nums[1] - nums[0]


        if nums[0] > nums[3]:
            b = nums[0] - nums[3]

        elif nums[3] > nums[0]:
            b = nums[3] - nums[0]


        if nums[1] > nums[2]:
            c = nums[1] - nums[2]

        elif nums[2] > nums[1]:
            c = nums[2] - nums[1]


        if nums[2] > nums[3]:
            d = nums[2] - nums[3]

        elif nums[3] > nums[2]:
            d = nums[2] - nums[3]

        y = 0
        for i in range(0, 4):
            x.forward(j)
            x.left(90)
            x.write(nums[y])
            y += 1

diamond()
