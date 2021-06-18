getemail = str(input ("What is your email adress?: \n"))
email = getemail.split("@")
email2 = (email[1])

while True:
    if email2 == "gmail.com":
        print ("Your email is hosted by Gmail")
    elif email2 == "yahoo.com":
        print ("Your email is hosted by yahoo")
    elif email2 == "mweb.co.za":
        print ("Your email is hosted by mweb")

    cont = str(input("Would you like to try another email adress?:\n")).lower()
    if cont == "yes":
        print ("okay, resuming... ")
        continue
    else : 
        break