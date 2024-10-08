score = 0
def Question(Que,Ans):
    
    
    if Que == Ans:
     print(" That right, the answer is " + Ans)
     score = int(score) + 1

    else:
        print(" That not the right answer, DumDum")

Question(input("What is the name of Disney's Mascot\n"),"Mickey Mouse")