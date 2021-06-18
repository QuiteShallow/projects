import time
import random
f = open("password_Storage.txt", "a")

def readfile ():
    while True:
        f = open("password_Storage.txt", "r")
        readfile = f.read()
        print ("==============")
        print (readfile)
        print ("==============")
        return 
        

nav = str(input("What would you like to do?:[Add New Passwords][Check Current Passwords]:\n")).lower()
while True:
    if nav != "add new passwords" or nav !="add new password" or nav !="check current password" or nav !="check current passwords":
        print ("error invalid option")
        str(input("continue?\n")) 
        continue

    elif nav == "check current passwords" or nav == "check current password":
        readfile()
        cont = str(input("Would you like to add a new password?[Yes][No]:\n")).lower()
        if cont == "yes":
            print ("okay loading application...\n")
            getno = int(input("What is the length of the password you would like to generate[Pick a number]:\n"))
            if getno > 8 or getno  < 1 :
                print ("invalid number")
            name = str(input("What will this password be used for?: \n"))
            idesc = str(input("Would you like to include a description for this password? [Yes][No]:\n")).lower()
            if idesc == "yes":
                desc = str(input("Input description here:\n"))
            elif idesc == "no":
                desc = "N/a"


            f.write (name + "|" + desc  +"\n")

            for x in range (0, getno):
                number = random.randint(0,100)
                letter = random.choice (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
                char = random.choice (['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', 
                '|', '}', '~'])
                
                pword = str(number) + str(letter) + str(char)
                print (pword)
                f.write (pword)

            f.write ("\n------------------------------------\n")

            print ("password succesfully added!")

        elif cont == "no":
            print ("Understood shutting down")
            break

    elif nav == "add new password":
        
        while True:
            print ("**********************************")
            print ("Welcome to the password generator!")
            print ("**********************************")

            getno = int(input("What is the length of the password you would like to generate[Pick a number]:\n"))
            if getno > 8 or getno  < 1 :
                print("invalid number")
            name = str(input("What will this password be used for?: \n"))
            idesc = str(input("Would you like to include a description for this password? [Yes][No]:\n")).lower()
            if idesc == "yes":
                desc = str(input("Input description here:\n"))
            elif idesc == "no":
                desc = "N/a"


            f.write (name + "|" + desc  +"\n")

            for x in range (0, getno):
                number = random.randint(0,100)
                letter = random.choice (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
                char = random.choice (['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', 
                '|', '}', '~'])
                
                pword = str(number) + str(letter) + str(char)
                print (pword)
                f.write (pword)

            f.write ("\n------------------------------------\n")

            cont = str(input("would you like to add a new password or view current passwords?[View][Yes][No]:")).lower()
            if cont == "yes":
                print ('okay loading')
                time.sleep(2)
                continue

            elif cont == "view":
                readfile()
                cont2 = str(input("Would you like to add a password?[Yes][No]:\n")).lower()
                if cont2 == "yes":
                    print("okay starting application...\n")
                    time.sleep(2)
                    continue
                elif cont == "no":
                    print ("Understood shutting down...")
                    time.sleep(2)
                    f.close()
                    break
                else :
                    pass
            
   
f.close()