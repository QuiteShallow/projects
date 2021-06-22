import time
f = open ('users.txt', "r")

def get_username (username):
    global fusername
    global fpassword
    f = open ('users.txt', 'r')
    read = f.readline()
    while read:
        uname = read.split("|") 
        if uname[0] == username:
             fusername = uname[0]
             fpassword = uname[1].rstrip()   
             return True 
        
        read = f.readline()
      

    f.close()
    return False


def register():
    f = open("users.txt", "a")
    username = input("Select a username")
    password = input("Select a password")
    concat = username + "|" + password
    f.write (concat + "\n") 
    print ("register sucesfull")
    f.close 

def start ():
    while True:
        direct = str(input("What would you like to do [register][login]")).lower()
        if direct != "login" and direct != "register":
            print (" invalid option ")
            continue
        else : 
            break

    if direct == "login":
        
         getname = input("What is your username?:\n")
         getpass = input("what is your password?:\n")

         if get_username(getname) == True and fpassword == getpass: 
             print ("login succesful")
         else :
             print ("login failed")


    elif direct == "register":

        register()


start()


f.close()