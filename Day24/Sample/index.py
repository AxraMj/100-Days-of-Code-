file = open("C:/Users/HP/100-Days-of-Code-/Day24/my_file.txt")
content =file.read()
print(content)
file.close() #to free up resource

#or
with open("C:/Users/HP/100-Days-of-Code-/Day24/my_file.txt") as file:
    content = file.read()
    print(content)

#by reading file with 'with' keyword then we no need
#to use close() because, it vertualy do the closing() functionality without manually writing
