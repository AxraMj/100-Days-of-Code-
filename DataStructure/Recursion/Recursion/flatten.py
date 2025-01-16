def flatten_list(nested_lit):
    new_list=[]
    for i in nested_lit:
        if isinstance(i,list):
            new_list.extend(flatten_list(i))
        else:
            new_list.append(i)
    return new_list



output=flatten_list([1,2,3,[4,5],[6,7]])
print(output)