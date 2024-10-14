#Exception Handling
#Write a program that add to number


#if  =  try
#else  =  except
def add():
    try:
        x = input("What is the first number:\n")  
        x = int(x)                                 
        y = input("What is the second number:\n")  
        y = int(y)                                 
        print(str(x) + " + " + str(y) + " = " + str( x + y)) 

    except:

        print("Nuh uh, you can't do that\n")
        add()
add()