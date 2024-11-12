#Loop control statments
#Allow you to change the loops operater
#Do things like quit a loop

fruit =["apple", "bug","strawberry", "watermelon", "pear"]

for fruit in fruit:
    if fruit == "bug":
        print("You found a bug in your fruit")
        break

    print("You ate a" + fruit)


order = [15, 21, 67, 21, 30 ,9, 43]
for order in order:
    print("$" + str(order) + "order discount 5% to $" + str(order * 0.95))