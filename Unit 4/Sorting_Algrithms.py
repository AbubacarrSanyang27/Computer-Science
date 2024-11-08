
import random
Num = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
print(Num)

def bubble_sort(number):
    steps = 0
    for j in range(0,len(Num) - 1):
      for i in range(0, len(number) - 1):
        if number[i] > number[i+1]:
            number[i], number[i+1]= number[i+1],number[1]
            steps += 1
            print()
         
def quick_sort(n):
   def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
    
    