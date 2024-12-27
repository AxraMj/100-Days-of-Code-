#step 1
import random
words=["Akshara","Avinash","Aiswarya","Akash"]

#TODO1: Randomly choose a word from the list and assign it to a variable called choosen_word
choosen_word= random.choice(words)
print(choosen_word)

#TODO2: Ask the user to guess a letter and assign it to a variable called guess. Make guess lowercase.
guess=input("Guess a letter: ").lower()
#TODO3: Check if the letter the user guessed (guess) is one of the letters in the choosen_word.
for letter in choosen_word:
    if letter==guess:
        print("Right")
        break
    else:
        continue
