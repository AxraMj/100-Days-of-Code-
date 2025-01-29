class Solution:
    def __init__(self):
        self.stack = []
        self.stackTwo=[]
        self.stackThree=[]
        self.list = [11, 22, 33, 44, 55, 66, 77, 88, 99] 

    def stack1(self):
        for i in range(0, len(self.list) // 3):
            self.stack.append(self.list[i])
        print("Stack One:", self.stack)

    def stack2(self):
        for i in range(len(self.list) // 3, 2 * len(self.list) // 3):
            self.stackTwo.append(self.list[i])
        print("Stack Two:", self.stackTwo)

    def stack3(self):
        for i in range( 2 * len(self.list) // 3, len(self.list)):
            self.stackThree.append(self.list[i])
        print("Third stack:" ,self.stackThree)



# Creating object of Solution class
obj = Solution()
obj.stack1()
obj.stack2()
obj.stack3()
