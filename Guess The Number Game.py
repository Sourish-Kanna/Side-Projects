# guess the number game
import random
n=random. randint (1, 100)
ctr=0
while ctr<5:
    guess=int(input ("Guess the number in range 1..100: "))
    if guess==n:
            print ("You won :)")
            break
    elif guess>100:
        print("Enter number less than 100")
        ctr+=1
    else:
        if n-15<guess<n:
            print("Number is little below")
        elif n<guess<n+15:
            print("Number is little above")
        elif n-15>guess:
            print("Number is below the number")
        elif n+15<guess:
            print("Number is above the number")
        ctr+=1
if not ctr<5:
    print ("You lose:( \nThe number was ", n)

import time
time.sleep(5)
