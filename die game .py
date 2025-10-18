#Die rolling game

import random

while True:
    a=input("wanna play? (y/n): ").lower()

    if a == "y":
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(f"({d1}, {d2})")
    
    elif a == "n":
        print("No problem.")
        break
    
    else:
        print("Error")


#completed