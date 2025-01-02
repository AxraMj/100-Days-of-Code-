import art
from replit import clear
import random


clear()
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_guess=random.randint(1,100)

easy_attempt=10
diff_attempt=5
start=True
difficulty_level=input("Choose Difficulty: type 'easy' or 'hard':")
if difficulty_level=='easy':
    print("You have 10 attempt to guess the number")
    while start:
        guess=int(input("Make a guess:"))
        if guess>computer_guess and easy_attempt!=0:
            print("Too high")
            print("Guess again")
            easy_attempt-=1
            print(f"You have {easy_attempt} attempt remaining to guess the number")
        elif guess<computer_guess and easy_attempt!=0:
            print("Too low")
            easy_attempt-=1
            print(f"You have {easy_attempt} attempt remaining to guess the number")
        elif guess==computer_guess:
            print("You Winn")
            break
        else:
            if easy_attempt==0:
                print("You have run out of attempts, You lose")
                break
elif difficulty_level=='hard':
    print("You have 5 attempt to guess the number")
    while start:
        guess=int(input("Make a guess:"))
        if guess>computer_guess and diff_attempt!=0:
            print("Too high")
            print("Guess again")
            diff_attempt-=1
            print(f"You have {diff_attempt} attempt remaining to guess the number")
        elif guess<computer_guess and diff_attempt!=0:
            print("Too low")
            diff_attempt-=1
            print(f"You have {diff_attempt} attempt remaining to guess the number")
        elif guess==computer_guess:
            print("You Winn")
            break
        else:
            if diff_attempt==0:
                print("You have run out of attempts, You lose")
                break
else:
    print("Invalid")
