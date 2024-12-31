from replit import clear
import art

print(art.logo)
bids={}
value=True
while value:
    names = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[names] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue=='yes':
        value=True
        clear()
    else:
        break
    

