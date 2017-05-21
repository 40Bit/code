import sys

state = {
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



            
def grasslandfile1():
    global state
    
    print("harvested 25 pieces of grass")
    answer11 = query_yes_no("craft grass-knitted pants?? ")

    if answer11:
        print("equipped grass-knitted pants.received 0.5 more speed")
        addspeed("speed", 0.5)
        eaglemountains()

    else:
        state["inventory"]["grass"] += 25
        print("inventory:")
        print(state["inventory"])
        eaglemountains()


def eaglemountains():
    global state
    
    for times in range(0, 3):

        
        answer16 = query_yes_no("take some rocks??")

        if answer16:
                print("took 3 rocks")
                state["inventory"]["rocks"] += 3
                print("this is what you have in inventory")
                print(state["inventory"])
                

        else:   
            print("this is what you have in inventory")
            print(state["inventory"])
            answer9 = query_yes_no("harvest grass from valley??")

            if answer9:
                print("you_________enemy")
                answer9 = query_yes_no("kill enemy??")
                
                if answer9:
                    print("you______//__<- enemy")
                    print("harvested 10 grass pieces")
                    state["inventory"]["grass"] += 10

                else:
                    print("you run up to the the higher cliffs")
                    print("_")
                    print(" _")
                    print("  _")
                    print("   ______'you___'enemy")
                    answer9 = query_yes_no("you see a spiked boomerang.do you take it??")

                    if answer9:
                        state["inventory"]["spiked boomerang"] += 1


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
                print("inventory:")
                print(state["inventory"])
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

