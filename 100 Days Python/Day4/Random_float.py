#random float
#definition: random float is a random number with a decimal point
#range: between 0 and 1

import random

random_float= random.random()
print(random_float) #prints a random float between 0 and 1

#to get a random float between 0 and 5
random_float = random.random()*5
print(random_float) #prints a random float between 0 and 5
#explaination: random.random() generates a random float between 0 and 1. To get a random float between 0 and 5, we multiply the random.random() by 5