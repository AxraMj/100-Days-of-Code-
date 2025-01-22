dic={'name': 'Alice', 'age': 25, 'city': 'New York'}
# dic.fromkeys(sequence[],value) syntax

print(dic)
new_dic=dic.fromkeys(['address','location'],'abc')
print(new_dic)

# {'name': 'Alice', 'age': 25, 'city': 'New York'}
# {'address': 'abc', 'location': 'abc'}

# 'abc': This is the value assigned to all the keys.