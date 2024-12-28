import random
import hangman_words
import hangman_art
from replit import clear
print(hangman_art.logo)
lives=6
random_word=random.choice(hangman_words.words)
display=[]
for _ in random_word:
    display.append("_") 

endpoint=False

while not endpoint:
    user_guess_letter=input("Guess the letter:")
    clear()
    print(f"You guessed letter {user_guess_letter} is in the word, So you are safe")
    if user_guess_letter in random_word:
        for possition in range(len(random_word)):
            letter=random_word[possition]
            if letter==user_guess_letter:
                display[possition]=letter   
        print(display)
        if "_" not in display:
            endpoint=True
            print("You win")
    else:
        print("You guessed letter is not in the word, So you lose a life")
        lives-=1
        print(hangman_art.stages[lives])
        if lives==0:
            endpoint=True
            print("You lose")

