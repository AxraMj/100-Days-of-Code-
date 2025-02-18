#-------------------Blackjack Project---------------------#
from replit import clear
import art
import random

start=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if start=='y':
    clear()
    print(art.logo)


def playing_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

user_card=[]
computer_card=[]

def deal_card():
    for _ in range(2):
        new_card=playing_cards()
        user_card.append(new_card)
        computer_card.append(new_card)
    return user_card,computer_card

deal_card()

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score>21:
        return "Opponent went over. You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_score=calculate_score(user_card)
    computer_score=calculate_score(computer_card)
    is_game_over=False

    while not is_game_over:
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal=='y':
                user_card.append(playing_cards())
                user_score=calculate_score(user_card)
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_card.append(playing_cards())
        computer_score=calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while start=='y':
    play_game()
    start=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if start=='y':
        clear()
        print(art.logo)
    else:
        print("Goodbye")
        break
#---------------------------------------------------------#
