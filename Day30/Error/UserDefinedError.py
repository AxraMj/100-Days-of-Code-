height=int(input("Enter the height:"))
weight=int(input("Enter the Weight:"))

if height > 3:
    raise ValueError("Human height should not be 3 meter more")


bmi=weight/height **2
print(bmi)