import time

repeat = int(input('How long do you want the timer to run?'))
min = 0
sec = 0
for x in range(repeat):
    sec = sec + 1
    
    if sec == 60:
        min = min + 1
        sec = sec - 60

    print (f"Seconds:{sec}|Minutes:{min}")
   
    time.sleep(0)

print ("Timer has ended")