for x in range (5):
    for y in range(5):
        if x == 0 or x == 4 or y == 0 or y == 4:
            print("*", end = (' '))
        elif x == 2 and y == 2 :
            print("k", end = " " )
        else:
            print(" ", end = " ")
    print()
