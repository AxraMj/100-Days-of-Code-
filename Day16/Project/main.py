from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_MoneyMachine=MoneyMachine()
my_CoffeeMaker=CoffeeMaker()
menu=Menu()
is_onn=True

my_MoneyMachine.report()
my_CoffeeMaker.report()

while is_onn:
    options=menu.get_items()
    choice=input(f"What would you like? ({options})")
    if choice=="off":
        is_onn=False
    elif choice=="report":
        my_CoffeeMaker.report()
        my_MoneyMachine.report()
    else:
        drink= menu.find_drink(choice)
        print(drink)

