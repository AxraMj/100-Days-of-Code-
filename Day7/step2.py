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

#Testing Code
print(f"psss...the choosen word is {choosen_word}")
#todo4: Create an empty list called display.
#  For each letter in the choosen_word, add a "_" to 'display'. So if the choosen_word was "apple", 
# display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.
display=[]
for _ in choosen_word:
    display+="_"

#todo5: Loop through each position in the choosen_word.
#  If the letter at that position matches 'guess', then reveal that letter in the display at that position.
#  e.g. If the user guessed "p" and the choosen_word was "apple", then display should be ["_","p","p","_","_"].
for position in range(len(choosen_word)):
    letter=choosen_word[position]
    if letter==guess:
        display[position]=letter
print(display)