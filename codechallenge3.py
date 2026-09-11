#PROBLEM: GLOBAL FREIGHT CALCULATOR


print("======================= PACKAGE DETAILS ==========================")
Y = "YES"
N = "NO"

print()
nth = (input("NAME OF THE SENDER: ")) #sender name
toi = (input("TYPE OF ITEMS:   "))# type of product

frag = (input("Is Fragile? (YES / NO): ")) #fragile
if frag == Y:
  print("Fragile: TRUE")
elif frag == N:
  print("Fragile: FALSE")
else:
  print("ANSWER UNRECOGNIZED")

wg = eval(input("Weight(kg):     ")) 
dis = eval(input("Distance(km):  ")) 

base_cost = (wg * 2.50) + (dis * 0.15)

ex = (input("Express? (YES / NO): "))

if ex == Y:
  print("Express: TRUE")

elif ex == N:
  print("Express: FALSE")

else:
  print(ex, "ANSWER UNRECOGNIZED")

int = (input("International? (YES / NO): "))

if int == Y:
  print("International: TRUE")

elif int == N:
  print("International: FALSE")

else:
  print("ANSWER UNRECOGNIZED")

if wg>= 1.5 and dis<= 50: #SHIPPING IS FREE
  total1 = 0.00

  print("The Shipping of item is Free, The Cost of Package: $",total1)

elif ex == Y and int == Y : #INTERNATIONAL AND EXPRESS
  total2 = (base_cost * 1.40) + 50

  print("The Item is Both International & Express, The Cost of the Package: $",total2)

elif wg>= 20 and ex == Y or int == Y : # EXPRESS / HEAVY INTERNATIONAL
  total3 = (base_cost * 1.20) + 25

  print("The Item is Express or Heavy International, The Cost of the Package: $",total3) 

elif wg>= 30 or dis>= 1000: #OVERSIZED / FAR
  total4 = base_cost + 30

  print("The Item is Oversized / Far, The Cost of the Package: $",total4)

else: 
  print("The Item Regular Rate: $", base_cost)

print("\n========== End of Transaction, Thankyou Customers!!! ===========")