#Rock Paper Scissors Game
import random
print("Welcome to Rock Paper Scissors Game")
choice=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors"))
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper=''' 
 _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_image=[rock,paper,scissors]
computer_choice=random.randint(0,2)
if choice==0:
    print(rock)
    print(f"Computer chose: {list_image[computer_choice]}")
    if computer_choice==0:
        print("It's a draw")
    elif computer_choice==1:
        print("You lose")
    else:
        print("You win")
elif choice==1:
    print(paper)
    print(f"Computer chose: {list_image[computer_choice]}")
    if computer_choice==0:
        print("You win")
    elif computer_choice==1:
        print("It's a draw")
    else:
        print("You lose")
else:
    print(scissors)
    print(f"Computer chose: {list_image[computer_choice]}")
    if computer_choice==0:
        print("You lose")
    elif computer_choice==1:
        print("You win")
    else:
        print("It's a draw")
print("Thank you for playing")
