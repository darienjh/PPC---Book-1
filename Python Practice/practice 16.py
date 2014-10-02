#darien hayes
#10/2/2014
#practicfe 16

import random
count = 1
random = random.randint(0,100)
guess = int(input("Guess the number: "))
while guess != random:
    if guess > random:
        print("Guess lower")
    if guess < random:
        print("Guess is higher")
    if guess == random:
        print("Well done!")
    count+=1
    guess = int(input("Guess the number: "))
    

#yes
#no
#no
#no
    
