#Booolean Expression
#Kinda like a mathimatical formula
#Can only be evaluate to true or fales
print(5 > 7)

#comparison operators: ==, <, ,> <=, >=
x = 5  #set x to 5
print( x == 5 )    #is x to 5

print( 4 >= 2) #True
print(1993 == 1993) #true
print( -99 > -90) #fales
print(10 != 10) #fales, "bash" "not"

#Boolean Expression Quiz
answer_one = input("Give a whole number that is equal than 5.\n")
answer_one = int(answer_one)
print(answer_one == 5)

print("Apple" == "Apple")

#take a temp
#print "[temp] is hot" if [temp] is greater than 81
#otherwise print "temp is not hot" 
temperature = input( "what is the temperature:\n")
if temperature >= 80:
    print(str(temperature) + "is hot")

if temperature < 80:
    print(str(temperature) + " is not hot")

else:
    print("that not a number")