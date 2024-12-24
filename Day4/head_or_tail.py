#Game: Head or Tail
#instructions
#you are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#the first letter should be capitalised and spelt exactly like in the example e.g. Heads, Tails
#there are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1.
#Then use that number to print out Heads or Tails.
#e.g.
#1 means Heads
#0 means Tails
#Example Output
#Heads
#or
#Tails
#Solution

import random
print("Welcome to the coin toss game")

coin=random.randint(0,1)

if coin == 1:
    print("Head")
else:
    print("Tails")
