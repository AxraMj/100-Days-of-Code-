def IsOddCheck(array):
    if len(array)==0:
        return False
    elif array[0]%2!=0:
        return True
    return IsOddCheck(array[1:])

print(IsOddCheck([4,6]))
print(IsOddCheck([1,2,4,6]))