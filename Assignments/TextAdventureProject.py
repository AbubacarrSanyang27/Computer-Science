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
    
    elif FolF1 == "stay":
        Find_F2()
    
    else:
        print(" Hint: try typing the word in the parenthesess")

def  WatchMov():
    print("Watch Movie")

def Fix_Power():
    print("Fix Power")

def Stay_Wait():
    print("Stay and wait")

def