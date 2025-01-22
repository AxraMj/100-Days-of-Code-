#Who will pay the bill?
#You are going to write a programgram which will select a random name from a list of names. 
#The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function.
#Line 8 splits the string names_string into individual names and puts them inside a List called names. 
#For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

import random

print("Who will pay the bill?")
name=["Akhil","Arun","Anand","Anoop","Anil","ashish", "Akshara","Avi","Aruna","Anu","Anjali","Anjana","Anjana"]
length=len(name)
random_name= random.randint(0,length-1)
print(f"{name[random_name]} will pay the bill today")
      