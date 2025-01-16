def RangeSolution(n):
    if n<0:
        return 0
    return n+RangeSolution(n-1)

output=RangeSolution(2)
print(output)
