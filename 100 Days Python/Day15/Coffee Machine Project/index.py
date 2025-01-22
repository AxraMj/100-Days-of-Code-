import Art
import data

print(Art.logo)
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

start=True
while start:
    user_choise=input("Press the Button? Press 'A' for ingredients And 'B' for Menu and 'F' for off:")
    if user_choise=='A':
        for i in resources:
            print(i,resources[i])
    elif user_choise=='B':
        menu_choice = input("​What would you like? (espresso($1.5)/latte($2.5)/cappuccino($3.0)): ")
        if menu_choice=='espresso' or menu_choice=='latte' or menu_choice=='cappuccino' :
            coin=input("Please insert coins.")
            if coin=='$1.5' or coin=='$2.5' or coin=='$3.0':
                print("Here is your order ☕️. Enjoy!")
            else:
                if coin>'$2.5' or coin >'$1.5' or coin>'$3.0':
                    print("Get balance")
                    print("Here is your order ☕️. Enjoy!")
                else:
                    print("Not sufficient amount to get drink")
    elif user_choise=='F':
        start=False



