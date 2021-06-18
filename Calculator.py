import time

being = str(input("Would you like to proceed to the calculator?:\n[Yes] [No]: \n")).lower()

if being == "yes":
    print ("Okay loading. . .")
    time.sleep (2)
elif being == "no":
    print ("Shutting Down")

x = True
while x == True :
    num1 = int(input("Insert the first number to be calculated here!: \n"))
    method = str(input("Input argument here!: [+][-][*][/]"))
    num2 = int(input("Input second number here"))

    if method == "+":
        print (num1 + num2)

    elif method == "-":
        print (num1 - num2)

    elif method == "/":
        print (num1 / num2)

    elif method == "*":
        print (num1 * num2)

    cont = str(input ("Would you like to calculate again?: \n"))
    if cont == "yes":
        print ("okay reloading Caclulator")
        time.sleep (2)
        continue
    else :
        break
