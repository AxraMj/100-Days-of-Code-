class users:
    def __init__(self):
        print("Created")

user1=users()
user1.name="Akshara"
user1.age=22
print(user1.name)

#if we have many object to create it will be very difficult to do so like this
user2=users()
user2.name="aB"
user2.age=22
print(user2.name)

#To avoid this we use constructor
#constructor is used to make object to perform task
#or it is used to initialize attributes