import random

stages=['''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
        |
        |
        |
-----------
''','''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
        |
        |
        |
-----------
''','''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
        |
        |
        |
-----------
''','''
    +---+
    |   |
    O   |
    /|   |
        |
        |
        |
        |
        |
-----------
''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
        |
        |
        |
-----------
''','''
    +---+
    |   |
    O   |
        |
        |
        |
        |
        |
        |
-----------
''','''
    +---+
    |   |
        |
        |
        |
        |
        |
        |
        |
-----------
''']
lives=6

words=["anil","sunil","soman"]
random_word=random.choice(words)
display=[]
for _ in random_word:
    display.append("_") 

endpoint=False

while not endpoint:

    user_guess_letter=input("Guess the letter:")
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
        lives-=1
        print(stages[lives])
        if lives==0:
            endpoint=True
            print("You lose")

