# activity13
age = int(input("How old are you? --> "))
is_employed = bool(input("Are you employed? (True/if not don't put any other answer) --> "))
cred_score = eval(input("What is your credit score? (0-1000) --> "))
annual_income = eval(input("What is your annual income? --> "))
print()
has_collateral = bool(input("Do you have any collateral? (True/if not don't put any other answer) --> "))

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
            elif annual_income < 40000:
                intt = 0.095
            elif has_collateral == True and annual_income < 40000:
                intt = 0.080              
            else:
                intt = 0.08
        else:
            print("Rejected: Credit score too low.")
            exit()
else:
        print("Rejected: Fails baseline criteria.")
        exit()
 

print("Interest: ", intt, "%")
