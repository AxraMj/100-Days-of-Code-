dic={'name': 'Alice', 'age': 25, 'city': 'New York'}

def searchelemnt(dic,value):
    for key in dic:
        if dic[key]==value:
            return "Value is present"
    return "Value not found"

print(searchelemnt(dic,25))