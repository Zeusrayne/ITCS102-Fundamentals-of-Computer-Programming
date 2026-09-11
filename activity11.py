#import demo
import getpass 

username = "zeus"
password = "ilabmyparents"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")


if u == username and p == password: 
	print("gagi tama, galing mo")

else: 
	print("holeeee, mali ikaw, pekeng zeus")