#playing with function

def student(name,age):
    print("Your Name:"+name)
    print("Age:"+age)

student("20","Akshara")
print("Check difference")
#output
# Your Name:20
# Age:Akshara     #This is called positional argument

#To overcome this positional argument use keyword Arguments

student(age="20",name="Akshara")