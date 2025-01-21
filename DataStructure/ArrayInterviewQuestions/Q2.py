#Write a program to find all pairs of integers whose sum is equal to given numbers

#[2,3,6,9,11] target=9 [3,6]

#Questions based on the problem is:
#1. Does array contain oly possitive and negative numbers?
#2. what if the same pair repeats twice , should we print it every time?
#3. if the reverse of the pair acceptable eg can we print both(4,1) and (1,4) if the given sum is 5
#4. do we need to print only distinct pairs? does(3,3) is a vlaid pair forgiven sum of 6?
#5. How big is the array?

def findPair(num,target):
    for i in range(len(num)):
        print(i)
        for j in range(i+1, len(num)):
            if num[i]==num[j]:
                continue
            elif num[i] + num[j] == target:
                print("")
mylist=[1,2,3,4,5]
findPair(mylist,5)