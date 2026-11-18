marvel = []

ans = input("Do you know any movie about marvel? (YES/NO) --> ").lower()

while True:
    
    if ans == "yes":
        title = input("What is the title of the marvel movie --> ")
        marvel.append(title)
        ans = input("Do you want to continue to give more marvel movie title? (YES/NO) --> ").lower()
    else:
        print(marvel)
        break
