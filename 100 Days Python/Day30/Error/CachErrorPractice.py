try:
    path="E:/100 Days Python/100-Days-of-Code-/Day30/Error/file.txt"
    f=open(path)
    list=[10,20,30]
    print(list[10])
except FileNotFoundError:
    print("No such file exist")
except IndexError:
    print("No such index")
else:
    print(list[1])
finally:
    f.close()