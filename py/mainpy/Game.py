import sys

state = {
    "hearts": 9,
    "speeds": {
        "speed": 0,
        "xspeed": 0,
    },
    "inventory": {
        "fabric": 0,
        "grass": 0,
        "rocks": 0,
        "x-speed hammmer": 0,
        "spiked boomerang": 0,
        "crystal": 0
        },
        
    }


# different methods

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def addspeed(type, add_speed):
    global state

    state["speeds"][type] += add_speed
    print("have %s %s" % (type, state["speeds"][type]))


def printstate(type):
    global state

    if (type == "hearts"):
        print("this is your health:")
    else:
        print("this is your " + type + ": ")

    print(state[type])


def grasslandfile1():
    global state

    print("harvested 25 pieces of grass")
    answer11 = query_yes_no("craft grass-knitted pants?? ")

    if answer11:
        print("equipped grass-knitted pants.received 0.5 more speed")
        addspeed("speed", 0.5)
        printstate("hearts")
        
        eaglemountains()

    else:
        state["inventory"]["grass"] += 25
        printstate("inventory")
        eaglemountains()


def eaglemountains():
    global state

    for times in range(0, 3):


        answer16 = query_yes_no("take some rocks??")

        if answer16:
                print("took 3 rocks")
                state["inventory"]["rocks"] += 3
                print("this is what you have in inventory")
                printstate("inventory")
                answer9 = query_yes_no("you see something shiny.do you take a closer look??")
                
                if answer9:
                    print("you take a closer look.you see some crystals")

                else:
                    print("you try to back away from the crystal but you can't.you go look at the shiny thing.it is some crystals.")
                          
                answer9 = query_yes_no("do you take the crystals??")

                if answer9:
                          state["inventory"]["crystal"] += 2
                          print("this is your inventory:")
                          printstate("inventory")
                          print("you then fall into a hole somehow.then you realize that the crystal was a trap.you were supposed to take the crystal and then fall in the hole is how the person who made this trap designed.you also got hurt from the fall")
                          print("depleted 1 heart")
                          state["hearts"] -= 1
                          printstate("hearts")

                else:
                    print("you went away from the crystals.for some reason the barrier went away (the thing that was blocking you) making it possible to go away from the crystals")
                    print("you_________enemy_")
                    answer9 = query_yes_no("do you kill the enemy??")

                    if answer9:                                                                                                                                                         
                        print("you_________enemy")
                        print("the enemy is still alive")
                        answer9 = query_yes_no("do you hit the enemy again??")

                        if answer9:
                            print("you______//_<-_enemy")

                    else:
                        print("the enemy hits you once.depleted 1.5 hearts")
                        state[hearts] -= 1.5
                        printstate("hearts")
        else:
            print("this is what you have in inventory")
            printstate("inventory")
            printstate("hearts")
            
            answer9 = query_yes_no("harvest grass from valley??")

            if answer9:
                print("you_________enemy")
                answer9 = query_yes_no("kill enemy??")

                if answer9:
                    print("you______//__<-_enemy")
                    print("harvested 10 grass pieces")
                    state["inventory"]["grass"] += 10
                    print("your inventory:")
                    printstate("inventory")

                else:
                    print("you run up to the the higher cliffs")
                    print("_")
                    print(" _")
                    print("  _")
                    print("   ______'you___'enemy")
                    answer9 = query_yes_no("you see a spiked boomerang.do you take it??")

                    if answer9:
                        state["inventory"]["spiked boomerang"] += 1
                        addspeed("speed", 2)

                    else:
                        print("you__________enemy")
                        answer9 = query_yes_no("you see another enemy.do you kill it??")

                        if answer9:
                            print("you___//_<-_enemy")
                            printstate("hearts")
                            printstate("inventory")

                        else:
                            print("enemy depleted 0.5 hearts")
                            state["hearts"] -= 0.5
                            
                            printstate("hearts")
                            printstate("inventory") 

                            
def n_y_hit_dummy(question):
    global state


    answer = query_yes_no(question)

    if answer:
        print("you      //  <- dummy")
        answer6 = query_yes_no("go to official training grounds??")
        if answer6:
            print("loading official training grounds")
            answer9 = query_yes_no("train??")

            if answer9:
                print("earned 3 speed levels")
                addspeed("speed", 3)

                print("loading grassland")
                print("grassland loaded")
                answer7 = query_yes_no("harvest some grass?? ")


                if answer7:
                    grasslandfile1()


                else:
                    print("you____________enemy")
                    answer8 = query_yes_no("kill enemy?? ")

                    if answer8:
                        print("you_______//____ <- enemy")

                    else:
                        print("you run away from the enemy")

            else:
                print("loading grassland")
                print("grassland loaded")
                answer7 = query_yes_no("harvest some grass?? ")


                if answer7:
                    grasslandfile1()


                else:
                    print("you____________enemy")
                    answer8 = query_yes_no("kill enemy?? ")

                    if answer8:
                        print("you_______//____ <- enemy")

                    else:
                        print("you run away from the enemy")


        else:
            print("loading grassland")
            print("grassland loaded")
            answer7 = query_yes_no("harvest some grass?? ")

            if answer7:
                grasslandfile1()


            else:
                print("you____________enemy")
                answer8 = query_yes_no("kill enemy?? ")

                if answer8:
                    print("you_______//____ <- enemy")

                else:
                    print("you run away from the enemy")

    else:
        print("you have not killed the dummy.")

        answer6 = query_yes_no("take fabric??(from dummy) ")

        if answer6:
            print("collected 6 fabric")
            answer10 = query_yes_no("craft fabric pants??")

            if answer10:
                print("put on fabric pants.received 0.5 more speed")
                addspeed("speed", 0.5)
                print("loading grassland")
                print("grassland loaded")
                grasslandfile1()

            else:
                state["inventory"]["fabric"] += 6
                printstate("inventory")
                print("loading grassland")
                print("grassland loaded")
                answer12 = query_yes_no("harvest some grass?? ")


                if answer12:
                    grasslandfile1()


                else:
                    print("you____________enemy")
                    answer13 = query_yes_no("kill enemy?? ")

                    if answer13:
                        print("you_______//____ <- enemy")

                    else:
                        print("you run away from the enemy")



        else:
            print("the dummy is just standing there")
            print("loading grassland")
            print("grassland loaded")
            answer14 = query_yes_no("harvest some grass?? ")


            if answer14:
                grasslandfile1()

            else:
                print("you____________hammer")
                answer15 = query_yes_no("get hammer?? ")

                if answer15:
                    print("you_-||_<- hammer")
                    print("you pick up the hammer.it is a x-speed hammer.you gain 1.3 x-speed.")
                    addspeed("xspeed", 1.3)
                    state['inventory']["x-speed"] += 1

                else:
                    print("you go away from the hammer")


def start():

    print("a")
    print("game")
    print("by")
    print("[40Bit]")


    print("——————")
    print("QUESTX")
    print("——————")

    answer = query_yes_no("melee??")
    if answer:
        print("melee » |")
        answer3 = query_yes_no("go to spike cove?? ")
        if answer3:
            print("loading spike cove")
            print("you->_sc_dummy")
        else:
            print("loading sunlight meadows")
            print("you->_sm_dummy")

        n_y_hit_dummy("hit dummy?")

    else:
        print("ranged ˘ |")
        answer2 = query_yes_no("go to dark caverns?? ")
        if answer2:
            print("loading dark caverns")
            print("you___________dc_dummy")
        else:
            print("loading sunshine rocks")
            print("you___________sr_dummy")

        n_y_hit_dummy("shoot dummy?? ")



start()

