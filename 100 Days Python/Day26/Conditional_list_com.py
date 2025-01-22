#conditional list comprehension
#syntax
# new_list=[new_item for item in list if test]
names=["Akshara","Akash","Avinash","Aiswarya"]
short_name=[name.upper() for name in names if len(name)< 7]
print(short_name)