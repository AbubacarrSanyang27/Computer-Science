
import random
Num = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
print(Num)

def bubble_sort(number):
    steps = 0
    for j in range(0,len(Num) - 1):
      for i in range(0, len(number) - 1):
        if number[i] > number[i+1]:
            number[i], number[i+1]= number[i+1],number[1]
            steps += 1
            print()
         
bubble_sort(Num)




