import sys

state = {
    "speed": 0,
    "xspeed": 0,
    "inventory": {
        "fabric": 0,
        "grass": 0,
        "rocks": 0,
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


def addspeed(add_speed):
    global state
    
    state["speed"] = state["speed"] + add_speed
    print("have %s speed" % state["speed"])


def addxspeed(add_xspeed):
    global state
    
    state["xspeed"] = state["xspeed"] + add_xspeed
    print("have %s xspeed" % state["xspeed"])



            
def grasslandfile1():
    global state
    
    print("harvested 25 pieces of grass")
    answer11 = query_yes_no("craft grass-knitted pants?? ")

    if answer11:
        print("equipped grass-knitted pants.received 0.5 more speed")
        addspeed(0.5)
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
                addspeed(3)
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
            answer10 = query_yes_no("craft fabric pants")

            if answer10:
                print("put on fabric pants.received 0.5 more speed")
                addspeed(0.5)
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
                    addxspeed(1.3)
                    
                else:
                    print("you go away from the hammer")
                        
            

# main body
            
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
        
            
