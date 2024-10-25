print("Welcome to Nightmare at Lock in")
friend_1 = input("Before we start choose a name for your first friend\n")
friend_2 = input("And now one for you second friend\n")
print("Alright, let the nightmare being")
print("  ")

def Enter():
    global friend_1
    global friend_2
    print("As you enter the school you spot your friends " + friend_1 + " and  " + friend_2 + " as you enter")
    print("You are all excited because you are all attending your school year lock in where all the students stay overnight in the school")
    print("The school has set up activites to do and you are deciding where to go first, " + friend_1 + " wants to go see a movie in the gym but " + friend_2 + " want to play games in the seience room\n")
    Act = input(" Do you want to go the gym to watch a movie ( Movie ) or go to the science room to play game ( Game )\n")
    Act = Act.lower()
    if Act == "movie":
        Gym()

    elif Act == "game":
        SciRoom()

    else:
        print(" Hint: try typing the word in the parenthesess")

def Gym():
    print("You decide to go watch a movie with " + friend_1 + ".")
    print("As the movie goes on " + friend_1 + " tap you on your shoulder, they hears something coming for the supply room\n")
    Inv = input(" Do you go investigate (Go) or let " + friend_1 + " go by themself(Stay)\n")
    Inv = Inv.lower()
    if Inv == "go":
        Investigate()
    
    elif Inv == "stay":
        WatchMov()
    
    else:
        print(" Hint: try typing the word in the parenthesess")

def SciRoom():
    print("You decide to go play games with " + friend_2 + ".")
    print("While playing game, the power goes out")
    print(" A group of kids volunteer to go down and fix the power\n")
    Power = input(" Do you go help fix the power (Fix) or let them do it (Stay)\n")
    Power = Power.lower()
    if Power == "fix":
        Fix_Power()
    
    elif Power == "stay":
        Stay_Wait()
    
    else:
        print(" Hint: try typing the word in the parenthesess")


def  Investigate():
    print("You decide to go investigate with " + friend_1 + ".")
    print()
    print("while investigating the noise, you find a hole in the wall where the sound is loudest")
    print(friend_1 +  " crawls into it after a bit you hear them scream")
    FolF1 = input(" Do you follow " + friend_1 + " into the hole (Follow) or do you go find help (Help)\n")
    FolF1 = FolF1.lower()
    if FolF1 == "follow":
        End1()
    
    elif FolF1 == "help":
        Find_F2()
    
    else:
        print(" Hint: try typing the word in the parenthesess")

def  WatchMov():
    print("You stay and watch the movie as your friend goes")
    print("After the movie, you realise that " + friend_1 + " never returned.")
    print("You go to the supply closet only to find that it’s locked\n")
    FindF1 = input(" Do you look for " + friend_1 + " (Find) or do you go see" + friend_2 + " (Leave)\n")
    FindF1 = FindF1.lower()
    if FindF1 == "find":
        FinF1()
    
    elif FindF1 == "leave":
        SciRoom()
    else:
        print(" Hint: try typing the word in the parenthesess")

def Fix_Power():
    print("You and the group fIx the power and start to head back")
    print("You see " + friend_1 + " as you're walking back, they doese’t say anything but gesture for you to follow them")
    Go_F1 = input("Do you go with F1,(Yes) or (No)\n")
    Go_F1 = Go_F1.lower()
    if Go_F1 == "yes":
        print("While you walk, F1 knocks you over the head with a hard object and you fall to the ground, as you fade out of consciousness, you see F1 smile.")
        End4()
   
    elif Go_F1 == "no":
        print("You walk back to the sceince room and tell " + friend_2 + " the event of you trip, you decide to go and see " + friend_1 + " with " + friend_2 + "")
        SciRoom()
    else:
        print(" Hint: try typing the word in the parenthesess")

def End4():
    print("Ending 1: Fall to the hands for a Friend")
    print("to be concluded...")

def Stay_Wait():
    print("As you wait, " + friend_2 + " recommend that the two of you go " + friend_1 + " in the gym")
    find_F1()

def find_F1():
    print("Once you make it to the gym you realize, it’s emty except for a faint red light coming from the supply closet")
    print("You and " + friend_2 + " enter the supply closet only to find that the light is coming from a hole in the wall, you can hear something coming from the hole")
    print("F2 enter the hole and gestures for you to follow")
    FolF2 = input(" Do you follow " + friend_2 + " (yes) or (no)\n")
    FolF2 = FolF2.lower()
    if FolF2 == "yes":
        End3()
    
    elif FolF2 == "no":
        print("Something inside you tell you not to go but you know you can’t leave your friend")
        End3()
    else:
        print(" Hint: try typing the word in the parenthesess")

def End3():
    print("Ending 3: You Enter the hole with F2")
    print("to be concluded...")

def End1():
    print("Ending 5: You Enter the hole with F1")
    print("to be concluded...")

def  Find_F2():
    print("You decide to go find F2 for help")
    print("As you head to the sceince, the power goes out.")
    Power2 = input(" Do you go help fix the power (Fix) or keep heading to the science room (SciRoom)\n")
    Power2 = Power2.lower()
    if Power2 == "fix":
        Fix_Power()
    
    elif Power2 == "sciroom":
        End2()
    
    else:
        print(" Hint: try typing the word in the parenthesess")

def FinF1():
    print("Find F1")

def End2():
    print("As you continue to the scince you start to notice thing moving inthe dark, your about to hit the scince room but suddenly sometime grabs your leg and you hit the ground. you try to look bedind you to see what grab your leg you realise that you can’t moving, you can feel darkness creep over you but you can’t do a thing and eventuly...")