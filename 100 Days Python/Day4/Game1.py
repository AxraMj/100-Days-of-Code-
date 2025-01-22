#randomisation and python lists
# definition: list is a collection of items in a particular order
# randomisation is a way to shuffle the list

import random
#what is module? module is a file containing python definitions and statements
user_number=int(input("Guess a number: "))
random_number = random.randint(1,5) #prints a random number between 1 and 10
print(f"The random number is {random_number}")

if user_number == random_number:
    print("You win!!!")
else:
    print("You lose!!")
