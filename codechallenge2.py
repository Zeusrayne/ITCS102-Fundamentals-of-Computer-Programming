#breakdown fix money value to PH 
# 1000, 500, 200, 100, 50, 20, 10, 5, 1

money = eval(input("Enter Money to DEPOSIT ---->>> ")) # int(), eval(), type()
print(type(money))
print("=========================== PH BANK DENOMINATION ============================ ")
print("Money to deposit --------------> " , money, "php")


Libo = money // 1000 #13, 10.265
libo_sukli = money % 1000

five_h = libo_sukli // 500
five_sukli = libo_sukli % 500 

two_h = five_sukli // 200
two_sukli = five_sukli % 200

one_h = two_sukli // 100
one_sukli = two_sukli % 100

fifty = one_sukli // 50
fifty_sukli = one_sukli % 50

bente = fifty_sukli // 20 
bente_sukli = fifty_sukli % 20

sampo = bente_sukli // 10
sampo_sukli = bente_sukli % 10

lima = sampo_sukli // 5
lima_sukli = sampo_sukli % 5

piso = lima_sukli // 1
piso_sukli = lima_sukli % 1

print()
print("\t 1000 -", Libo)
print("\t  500 -", five_h)
print("\t  200 -", two_h)
print("\t  100 -", one_h)
print("\t   50 -", fifty)
print("\t   20 -", bente)
print("\t   10 -", sampo)
print("\t    5 -", lima)
print("\t    1 -", piso)