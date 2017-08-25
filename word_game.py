
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

while fails > 5:
    print("y_o|u__l|o_s|e_")
    print("y|o_u|_l_o|s_e|")
    
