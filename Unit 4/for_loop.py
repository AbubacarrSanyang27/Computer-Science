#For Loops
#This is a BIG deal
#For loops allow the programer to repeat or what we call loop

for i in range(0,10):
    print(i)


topMinecraft_Weapon = ["Mace", "Sword", "Trident", "Bow", "Axe"]

for Weapon in topMinecraft_Weapon:
    print(Weapon)



import random
sum = 0
Num = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100), ]
print(Num)
for Number in Num:
     sum += Number
print(sum)
