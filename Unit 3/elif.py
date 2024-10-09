x = 5

if x > 0:
    print("x is a positive number")

elif x < 0:
    print("x is a negitive number")

else:   #else are always paired with if
        # else never take a conditon
    print(" x is zero")


color = input("What color is the light:\n")
if color.lower() == "green":       #only 1
    print("Go")

elif color.lower () == "yellow":    #unlimited
    print( "Get Ready to stop")

elif color.lower() == "red":
    print("Stop")
else:           #only 1
    print("GUN IT")    