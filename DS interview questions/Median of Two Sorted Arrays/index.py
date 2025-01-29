# Median of Two Sorted Arrays
a=[1,2,3]
b=[4,5,6]
c=a+b

n=len(c)
if n%2==1:
    median=c[n//2]
else:
    median = (c[(n // 2) - 1] + c[n // 2]) / 2

print("Median:", median)
