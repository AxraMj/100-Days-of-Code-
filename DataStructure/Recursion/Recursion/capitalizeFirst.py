def capitalisefirst(array):
        result=[]
        if len(array)==0:
                return result
        result.append(array[0][0].upper() +array[0][1:])
        return result+capitalisefirst(array[1:])
 

print(capitalisefirst(["hello","hi","howare you"]))     