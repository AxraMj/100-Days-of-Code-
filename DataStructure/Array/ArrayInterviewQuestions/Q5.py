#Permutation

def permuation(list1,list2):
    if len(list1)!= len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False
    
list1=['a','c','b']
list2=['c','a','b']
print(permuation(list1,list2))