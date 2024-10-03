word1 = input("What your first word:\n")
word2 = input("What your second word:\n")
word3 = input("What your third word:\n")
print(word1 + word2 + word3)




def add_three(P1, P2, P3):
 Sum = ( P1 + P2 + P3)
 print(Sum)

N1 = input( "Chooses a number:\n" )
N1 = int(N1)
N2 = input( "Chooses a second number:\n" )
N2 = int(N2)
N3 = input( "Chooses a third number:\n" )
N3 = int(N3)
add_three(N1, N2, N3)




def data_three():
     num = input("Write a number:\n")
     num = int(num)
     wor = input("Write a word:\n")
     wor = str(wor)
     flo = input("Write a decimal:\n")
     flo = float(flo)
     FN = flo + num 
     FN = str(FN)
     print( FN + wor)

data_three()