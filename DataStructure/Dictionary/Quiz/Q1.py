# Q-1. What will be the output of the following code snippet?
a = {(1,2):1,(2,3):2}
print(a[1,2])

# A. Key Error
# B.  1 ✔️
# C. {(2,3):2}
# D. {(1,2):1}

# Explanation:
# The dictionary a has two keys: (1, 2) with the value 1, and (2, 3) with the value 2.
# When you write a[1, 2], Python interprets it as a[(1, 2)] because a tuple can be written without 
# parentheses when used in this way.