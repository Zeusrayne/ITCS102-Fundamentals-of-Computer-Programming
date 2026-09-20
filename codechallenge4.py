# codechallenge4
import getpass

acc = "zeushandsome"
password = "password1"

login_acc = input("Account Username: --> ")
login_pass = getpass.getpass("Password: --> ")
print()

if login_acc == acc and login_pass == password:
    Name = input("What is your name --> ")
    jobdesc = input("What is your job? --> ")
    age = int(input("How old are you? --> "))
    is_employed = bool(input("Are you employed? (True/if not don't put any other answer) --> "))
    cred_score = eval(input("What is your credit score? (0-1000) --> "))
    annual_income = eval(input("What is your annual income? --> "))
    print()
    has_collateral = bool(input("Do you have any collateral? (True/if not don't put any other answer) --> "))

    if has_collateral == True:
        item_col = input("What item is your collateral? --> ")
        value_col = eval(input("How much is your collateral? --> "))

        if value_col >= 30000:
            has_col = True
        else:
            has_col = False
    else:
        item_col = "None"

    print()
    if (age >= 21 and age <= 65) and is_employed == True:
        if cred_score >= 750:
            if annual_income >= 100000:
                intt = 0.045
                inp = intt * 100
            else:
                intt = 0.05
                inp = intt * 100
        elif 600 <= cred_score < 750:
            if has_collateral == True:
                intt = 0.07
                inp = intt * 100
            elif annual_income < 40000:
                intt = 0.095
                inp = intt * 100
            elif has_collateral == True and annual_income < 40000:
                intt = 0.080
                inp = intt * 100
            else:
                intt = 0.08
                inp = intt * 100
        else:
            print("Rejected: Credit score too low.")
            exit()
    else:
        print("Rejected: Fails baseline criteria.")
        exit()
    loan = eval(input("How much do you want to loan? --> "))
    print()
    print("First Name: ", Name)
    print("Money loaned: ₱", loan)
    print("Interest: ", inp, "%")
    print("Money Interest: ₱", loan * intt)
    print("Loan with Interest: ₱", loan + (loan * intt))
    print("Item Collateral: ", item_col)
    print("Value Collateral: ", value_col)
else:
    print("Account username/password is incorrect.")

print()
