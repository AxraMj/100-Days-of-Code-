
# Q-7. What will be the output of the following code block?

l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0]) 

print(init_tuple)
# A. ()
# B. (‘Python’)
# C. (‘Python’, ‘Python’)
# D. Runtime Exception.
 

