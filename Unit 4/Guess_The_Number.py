import random
Number = random.randint(0,100)
print(Number)
Entered = 0
Attempt = 0
while Number != Entered:
     entered = int(input("Please enter your number\n>"))
     Attempt = Attempt + 1

     if Entered < Number:
        print("Too low, try again")
     elif Entered > Number:
        print("Too high, try again")
     elif Entered == Number:
         print("That right the number was " + str(Number) + ", good job")
         print("It took you" + Attempt + " trys")
     else:
         print("get out")