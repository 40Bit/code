input1:

z = "_"
a = "_"
p = "_"

fails = 0


# if answer = z, 1 = z
# print (z)
# print (a)
# print (p)

while fails < 5:

    answer5 = input("guess a letter(or a word!)")

    if answer5 == "z":
                z = "z"

    elif answer5 == "a":
                a = "a"

    elif answer5 == "p":
                p = "p"

    elif answer5 == "zap":
        z = "z"
        a = "a"
        p = "p"
    

    else:
        fails += 1
            
    print(z)
    print(a)
    print(p)

    print("fails:")
    print(fails)
