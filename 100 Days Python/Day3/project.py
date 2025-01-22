#Tressure Island
print(''' 
*******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    |           |       |o;  ;   __ _`o       `"=.`_-"o; ;  |
    |___________|_______| |  |   O// .;        (o;  ;  |  |
    |           |       |o;  ;    ;` `;         | ;  ;  ;  |
    |___________|_______| |  |     |   |         |  |   |  |
    |           |       |o; ;     |   |         |  ;   |  |
    |___________|_______|  |  `----'   |          |   `----'
*******************************************************************************
 ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()

if direction == "left":
    print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    action = input().lower()
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        color = input().lower()
        if color == "yellow":
            print("You found the treasure! You Win!")
        elif color == "red":
            print("It's a room full of fire. Game Over.")
        elif color == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")

