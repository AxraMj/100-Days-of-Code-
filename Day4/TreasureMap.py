#Treasure Map
# Instructions
# You are going to write a program which will mark a spot with an X.
#the map is made of 3 rows
#your program should allow to enter the possition of the treasure usig a two digit system.
#the first digit is the vertical column number and the second digit is the horizontal row number.
#colum 2 , row 3 would be 23

print("Welcome to Treasure Map")
row1=["⬜️","⬜️","⬜️"]
row2=["⬜️","⬜️","⬜️"]
row3=["⬜️","⬜️","⬜️"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? ")
column=int(position[0])
row=int(position[1])
map[row-1][column-1]="X"
print(f"{row1}\n{row2}\n{row3}")
