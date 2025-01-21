fruits=["apple","pear","orange"]
#TODO: catch the exception and make sure the code

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("no such index value")
    else:
        print(fruit + "pie")

make_pie(7)