import time
import random
getname = str(input("What would you like to be called?:\n"))
best_of = int(input("How many rounds would you like to play?:\n"))
comscore = 0
myscore = 0


for x in range (best_of):
    myaction = str(input("What would you like to play?[Rock][Paper][Scissors]:\n")).lower()
    comaction = random.choice (['Rock','Paper',"Scissors"]).lower()

    if myaction == comaction:
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("its a tie!")
        print ("-----------------------------------------------")
        time.sleep(.250)
    
    #Rock combinations
    if myaction == "rock" and comaction == "paper":
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("Compter has won this round!")
        comscore = comscore + 1
        print (f"Score:\nCom:{comscore}\n{getname}:{myscore}")
        print ("-----------------------------------------------")
        time.sleep(.250)
        

    if myaction == "rock" and comaction == "scissors":
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("player has won this round")
        myscore = myscore + 1
        print (f"Score:\nCom:{comscore}\n{getname}:{myscore}")
        print ("-----------------------------------------------")
        time.sleep(.250)
        
        

    #paper combinations
    if myaction == "paper" and comaction == "scissors":
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("Computer has won this round")
        comscore = comscore + 1
        print (f"Score:\nCom:{comscore}\n{getname}:{myscore}")
        print ("-----------------------------------------------")
        time.sleep(.250)
        
        
    
    if myaction == "paper" and comaction == "rock":
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("player has won this round")
        myscore = myscore + 1
        print (f"Score:\nCom:{comscore}\n{getname}:{myscore}")
        print ("-----------------------------------------------")
        time.sleep(.250)
        
        

    #Scissors combinations
    if myaction == "scissors" and comaction == "rock":
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("computer has won this round!")
        comscore = comscore + 1
        print (f"Score:\nCom:{comscore}\n{getname}:{myscore}")
        print ("-----------------------------------------------")
        time.sleep(.250)
    

    if myaction == "scissors" and comaction == "paper":
        print (f"{getname}:{myaction} vs com:{comaction}")
        print ("player has won this round") 
        myscore = myscore + 1   
        print (f"Score:\nCom:{comscore}\n{getname}:{myscore}")
        print ("-----------------------------------------------")
        time.sleep(.250)
        
        

if comscore > myscore:
    print ("the computer has won this set of rounds!")
elif myscore == comscore:
    print ("This set of rounds ended in a tie!")
else : 
    print (f"{getname} has won this set of rounds!")

