#for loop range function
#definition of range function
#what is range function? 
# range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#range(start, stop, step)
#start: Optional. An integer number specifying at which position to start. Default is 0 
#stop: Required. An integer number specifying at which position to stop.
#step: Optional. An integer number specifying the incrementation. Default is 1
#Example
# for x in range(6):
#   print(x)
#Output
#0 1 2 3 4 5
#Example
# for x in range(2, 6):
#   print(x)
#Output
#2 3 4 5
#Example
# for x in range(2, 30, 3):
#   print(x)
#Output
#2 5 8 11 14 17 20 23 26 29


#sum of 100 numbers
sum=0
for n in range(1,101):
    sum += n
print(sum)
