#There are a couple types of loops in python
#The for loop lets your iterate a list
# -great for looping a set amount of times
#BUT WHAT IF we need to iterate an uncerteain amount of times
#ex. Entering your password

real_pasword = "noob69"
entered = ""
Attempt = 0
while real_pasword != entered:
    entered = input("Please enter your password\n>")
    Attempt = Attempt + 1

    if entered == real_pasword:
        print("Access Granted")
    else:
        print("Access Denied, Try Again")
        print("You have had" + Attempt + " attempts.")

print("Welcome!")

user_input = ""
while user_input != "exit":
    