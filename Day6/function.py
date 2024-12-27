#Function
#Definition of function: A function is a block of organized, reusable code that is used to perform a single, related action. 
# Functions provide better modularity for your application and a high degree of code reusing.
# As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions.
# These functions are called user-defined functions.

#some built-in functions are:
#1. abs()	Returns the absolute value of a number
#2. all()	Returns True if all items in an iterable object are true
#3. any()	Returns True if any item in an iterable object is true
#4. ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
#5. bin()	Returns the binary version of a number
#6. bool()	Returns the boolean value of the specified object

#some known built-in functions are:
#1. print()	Prints the specified message to the screen
#2. input()	Allows user input
#3. int()	Returns an integer number
#4. len()	Returns the length of an object
#5. list()	Returns a list
#6. max()	Returns the largest number
#7. min()	Returns the smallest number
#8. open()	Opens a file and returns a file object
#9. range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
#10. round()	Rounds a numbers
#11. set()	Returns a new set object
#12. str()	Returns a string object
#13. sum()	Sums the items of an iterator
#14. tuple()	Returns a tuple
#15. type()	Returns the type of an object
#16. zip()	Returns an iterator, from two or more iterators

#--------------------------------------------------------------------------------------------------------------
#user-defined functions
#syntax:
#def function_name(parameters):
#    """docstring"""
#    statement(s)
#def keyword is used to define a function in python.
#function_name: This is the name of the function.
#parameters (arguments): A function may optionally take one or more parameters.
#docstring: This is the first string after the function header. This string is used to document the function.
#statement(s): The code which is to be executed by the function.

#example:
def my_function(): #function without parameter
    print("hello")
    print("Hi")

my_function() #calling function


