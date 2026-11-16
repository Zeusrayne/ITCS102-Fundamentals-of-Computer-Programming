#codechallenge9

print("Task #1")
loan = float(input("Input the loan ammount: $"))
years = int(input("Input the loan period in years: "))

months = years * 12
rate = 0.03
principal = loan / months
remaining = loan


print("\nPayment Schedule")
print("Month |\t Payment\t|\tInterest\t|\tPrincipal\t|\tRemaining Loan")
print("===============================================================================================")

for month in range(1, months + 1):

    interest = remaining * rate / 12
    payment = principal + interest
    remaining = remaining - principal

    if month == months:
        remaining = 0

    print(f"{month:5} |\t ${payment:.2f} \t|\t ${interest:.2f}  \t|\t ${principal:.2f}  \t|\t ${remaining:.2f}")

print("----------------------------------------------------------------------------------------------")
print("\n\n\n\nTask #2")

for x in range(7):
    for y in range(13):
        if y == 6 - x or y == 6 + x or x == 6:
            print("*", end = "")
        else:
            print("", end = " ")

    print()

print("----------------------------------------------------------------------------------------------")
print("\n\n\nTask #3")

for x in range(5):
    for y in range(5):
        if x == 0 or x == 4 or x + y == 4:
            print("*", end = "")
        else:
            print("", end = " ")

    print()