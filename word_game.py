
z = "_"
a = "_"
p = "_"

fails = 0




# if answer = z, 1 = z
# print (z)
# print (a)
# print (p)

while fails < 9:

    answer5 = input("guess a letter(or a word!)")

    for x in answer5:
        
        if x == "z":
            z = "z"

        elif x == "a":
            a = "a"

        elif x == "p":
            p = "p"
        

        else:
            fails += 1
                
    print(z)
    print(a)
    print(p)

    print("fails:")
    print(fails)
