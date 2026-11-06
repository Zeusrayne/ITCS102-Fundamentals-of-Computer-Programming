#getpass import getpass

login = False 
loginattempt = 0

z = "manalopogi"
x = "kulotskie"

while login == False:
    username = input("input your username -->:")
    pssword = input("input your password -->:") 

    if username == z and pssword == x:
        print("Loginsuccesfully")
        print("Total login attempt :", loginattempt)
        login = True
    else: 
        print("incorrect username and password")
        loginattempt += 1
        login = False
print ()

