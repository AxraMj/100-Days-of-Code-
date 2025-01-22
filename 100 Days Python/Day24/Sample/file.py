with open("C:/Users/HP/100-Days-of-Code-/Day24/my_file.txt",mode="w") as file:
    file.write("New text to write")

#without deleting the content inside the text file add content then we need to use mode="a" 
#which means append

with open("C:/Users/HP/100-Days-of-Code-/Day24/my_file.txt",mode="a") as file:
    file.write("\nadd this also")

#to create a new file
with open("C:/Users/HP/100-Days-of-Code-/Day24/my_file2.txt",mode="w") as file:
    file.write("New text to write")