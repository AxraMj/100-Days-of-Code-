dic={'name': 'Alice', 'age': 25, 'city': 'New York'}
# sorted(iterable,reverse=,key=)

print(sorted(dic,reverse=True))
# ['name', 'city', 'age']

print(sorted(dic,key=len))
# ['age', 'name', 'city']  sorted based on char len