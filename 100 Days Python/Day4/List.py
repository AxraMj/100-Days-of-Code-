#list
# definition: list is a collection of items in a particular order
# list is a data structure in python that is mutable, or changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item.
# Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].
# Lists are great to use when you want to work with many related values.
# list is a collection which is ordered and changeable. Allows duplicate members.
# why list is a data structure? because it is a collection of elements that are stored in a particular order.
import random
state_of_kerala=["kottayam","kochi","trivandrum","kannur","kollam"]
print(random.choice(state_of_kerala))

print(state_of_kerala[0])
state_of_kerala.append("palakkad")
print(state_of_kerala)

