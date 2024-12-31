from replit import clear
import art

print(art.logo)
bids={}

def find_height_bider(bid_rectord):
    # bidding_record = {"Angela": 123, "James": 321}
    highest_bid=0
    winner=""

    for bidder in bid_rectord:
        bid_ammount=bid_rectord[bidder]
        if bid_ammount>highest_bid:
            highest_bid=bid_ammount
            winner=highest_bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")

value=True
while value:
    names = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[names] = price #adding keyvalues to the bid dictionary
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue=='yes':
        value=True
        clear()
    else:
        find_height_bider(bids)
        break
    

