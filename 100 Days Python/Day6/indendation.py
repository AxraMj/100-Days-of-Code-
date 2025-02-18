#indentation
#definition: 
# Indentation refers to the spaces at the beginning of a code line. 
# Where in other programming languages the indentation in code is for readability only,
# the indentation in Python is very important. Python uses indentation to indicate a block of code.
#example:
#-----------------------------------
# def my_function():                |
#     print("hello")                | this is indentation / block of code
#-----------------------------------|
#print("Hi")

#complex example:
#-----------------------------------
# def my_function():                |
#     print("hello")                | this is indentation / block of code
#     if True:                      |
#         print("Hi")               |
#-----------------------------------|
# print("Hello")

#Note: Indentation can be done using space or tab but not both.

#more complex example:
#-----------------------------------
# def my_function():                |
#     print("hello")                | this is indentation / block of code
#     if True:                      |
#         print("Hi")               |
#         if True:                  |
#             print("Hello")        |
#-----------------------------------|
# print("Hello")


#-----------------------------------
# def my_function():                |
#     print("hello")                | this is indentation / block of code
#     if True:                      |
#         print("Hi")               |
#         if True:                  |
#             print("Hello")        |
#             if True:              |
#                 print("World")    |
#             else:                  |
#                 print("Python")   |
#-----------------------------------|
