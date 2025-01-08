class Animal:
    def __init__(self):
        self.eyes_color="blue"
    
    def breath(self):
        print("inhale,exhale")

    def Feeding(slef):
        print("Hungry!!search for food")

#inherit

class Fish(Animal):
    def __init__(self):
        super().__init__()
    #need to add more feature on inherited content

    def breath(self):
        super().breath()
        print("Under water")
    

    def swim(self):
        print("Can swim")

nemo=Fish()
nemo.breath()
nemo.Feeding()
nemo.swim()

        

