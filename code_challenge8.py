#code challenge 8

rows = int(input("Put any number of rows you want: "))

for m in range(rows - 1):
    for o in range(m, rows):
        print(" ", end=" ")
    
    for o in range(x):
        print("*", end=" ")
        
    for o in range(x + 1):
        print("*", end=" ")        
    print()    
    
for m in range(rows):
    for o in range(m + 1):
        print(" ", end=" ")
    
    for o in range(m, rows - 1):
        print("*", end=" ")
        
    for o in range(m, rows):
        print("*", end=" ")        
    print()    
