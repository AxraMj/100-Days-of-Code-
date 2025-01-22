import Art
from game_data import datas
from replit import clear
import random

def format_data(accounts):
    """Format the account data into printable format"""
    account_name=accounts["name"]
    account_des=accounts["description"]
    account_country=accounts["country"]
    return f"{account_name},a {account_des}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
    """Take the user guess and followers count and return if they got right"""
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"


print(Art.logo)
score=0
game_should_continue=True
accounts_B=random.choice(datas)

while game_should_continue:
    clear()
    accounts_A=accounts_B
    accounts_B=random.choice(datas)

    if accounts_A==accounts_B:
        accounts_B=random.choice(datas)

    print(f"Compare A: {format_data(accounts_A)}.")
    print(Art.vs)
    print(f"Compare B: {format_data(accounts_B)}.")


    guess= input("Who has more Followers?Type 'A' or 'B': ").lower()

    a_folower_count=accounts_A["follower_count"]
    b_folower_count=accounts_B["follower_count"]

    is_correct=check_answer(guess,a_folower_count,b_folower_count)

    if is_correct:
        score+=1
        print(f"You are right!, Currect score: {score}")
    else:
        game_should_continue=False
        clear()
        print("Sorry, You are Wrong!!")