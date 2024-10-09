Hurricane_Speed = input("What is the Speed of the Hurrican:\n")
Hurricane_Speed = int(Hurricane_Speed)

if Hurricane_Speed < 74:
    print("This is a tropical storm")

elif Hurricane_Speed < 96:
    print("This is a Category 1")

elif Hurricane_Speed < 111:
    print("This is a Category 2")

elif Hurricane_Speed < 130:
    print("This is a Category 3")

elif Hurricane_Speed < 157:
    print("This is a Category 4")

elif Hurricane_Speed >= 157:
    print("This is a Category 5")

else:
    print("That's...I can't...get out.")