dic={'name': 'Alice', 'age': 25, 'city': 'New York'}
#dic.setdefault(key,default_value) syntax


# The setdefault() method in Python dictionaries is used to retrieve the value of a specified key. 
# If the key is not present in the dictionary, it inserts the key with a 
# specified default value and then returns that default value.

dic.setdefault('country', 'USA')

print(dic)

# {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}