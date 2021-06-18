import random
import time

rnum = random.randint (1, 10)

for x in range (0, 5):
    rem = x 
    print (rnum)
    guess = int(input("Take a guess at what the number is: \n"))
    if guess == rnum:
        print ("You have guess correctly!!")
        break
    elif guess > rnum:
        print ("The number you've guessed is too high try again!: \n")
    else :
        print ("The number you've guessed is too low, try again!: \n") 

    time.sleep (2)
    
