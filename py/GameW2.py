import time

state = {"inventory": {"axe": 0, "wood": 0, "slime_jelly": 0}}

def start3():
    answer = ""
    print("skip")

def inventorypr(add1, add2):
    state["inventory"][add1] += add2
    time.sleep(1.5)
    print("this is your inventory:")
    print(state["inventory"])   

def load():
    print("loading..10%")
    time.sleep(.500)
    print("loading..20%")
    time.sleep(.500)
    print("loading..30%")
    time.sleep(.500)
    print("loading..40%")
    time.sleep(.500)
    print("loading..50%")
    time.sleep(.500)
    print("loading..60%")
    time.sleep(.500)
    print("loading..70%")
    time.sleep(.500)
    print("loading..80%")
    time.sleep(.500)
    print("loading..90%")
    time.sleep(.500)
    print("loading..100%")
    print("loaded")
    time.sleep(.500)


def start():

    answer = ""
    print("                                                       |D") 
    print("you are a captain, on a boat trying to find new land <_|> <- your boat")
    time.sleep(1.5)
    print("a storm occurs and you crash on island Haled")
    time.sleep(1.5)
    print("[location1] island Haled")
    time.sleep(1.5)
    print("you see an axe")
    time.sleep(1.5)

    while answer == "":
        answer = input("do you take the axe? [y/n]")
        

        if answer == "yes":
            print("you take the axe")
            inventorypr("axe", 1)
            start2()
            

        elif answer == "no":
            print("you walk away from the axe")
            start2()

        else:
            answer = ""
        
def start2():
    answer = ""
    if state["inventory"]["axe"] > 0:
        print("you see a tree")
        time.sleep(1.5)

        while answer == "":
            answer = input("cut tree??? [y/n]")

            if answer == "yes":
                print("you cut the tree down")
                inventorypr("wood", 5)
                time.sleep(1.5)
                print("after you cut the tree, you see a slime")
                time.sleep(1.5)
                if state["inventory"]["axe"] > 0:
                    while answer == "":
                        answer = input("kill slime??? [y/n]")

                        if answer == "yes":
                           inventorypr("slime_jelly", 3)

                        if answer == "no":
                            start3()

                        else:
                            answer = ""
                        
                

            elif answer == "no":
                print("you walk away from the tree")
                start3()
                
            else:
                answer = ""

        
    if state["inventory"]["axe"] == 0:
        print("skip")
        start3()
    
    
answer = ""

print("a")
print("game")
print("by")
print("[40Bit]")
print("~-~-~WAVE~-~-~")

while answer == "":
    answer = input('type "a" to continue ')

    if answer == "a":

        load()
        start()

    else:
        answer = ""
        
