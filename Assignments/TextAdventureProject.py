print("Welcome to Nightmare at Lock in")
F1 = input("Before we start choose a name for your first friend\n")
F2 = input("And now one for you second friend\n")
print = ("Alright, let the nightmare being")

def Enter():
    print("As you enter the school you spot your friends " + F1 + " and  " + F2 + " as you enter")
    print("You are all excited because you are all attending your school year lock in where all the students stay overnight in the school, the school has set up activites to do and you are deciding where to go first, " + F1 + " wants to go see a movie in the gym but " + F2 + " want to play games in the seience room")
    Act = input(" Do you want to go the gym to watch a movie ( Movie ) or go to the science room to play game ( Game )")
    Act = Act.lower()
    if Act == "movie":
        Gym()

    elif Act == "game":
        SciRoom()

    else:
        print(" Hint: try typing the word in the parentices")

def Gym():
    print("movie")

def SciRoom():
    print("game")


Enter()