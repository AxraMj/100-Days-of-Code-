class users:
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
        self.follower=0
        self.following=0
    def perform_follow(self,user):
        user.follower+=1
        self.following+=1

user1=users(1,"Akshara")
user2=users(2,"Avi")

user1.perform_follow(user2)
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)