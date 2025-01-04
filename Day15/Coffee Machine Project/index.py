import Art
import data

print(Art.logo)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
repete=True
while repete:
    users_choice=input("What would you like? (espresso/latte/cappuccino): ")
    if users_choice=='report':
        for i in resources:
            print(i  , resources[i])
    elif users_choice=='espresso':
        print("Please insert coins.")
        Coin_insert=input("cost $1.5 ?: ")
        if Coin_insert!='1.5':
            print("Not sufficient money, money refunded")
    elif users_choice=='latte':
        print("Please insert coins.")
        Coin_insert=input("how many ?: ")
    elif users_choice=='cappuccino':
        print("Please insert coins.")
        Coin_insert=input("how many ?: ")
    else:
        print("Invalid")


