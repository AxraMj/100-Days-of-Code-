fruit_list1=['apple','orange','cherry','pappaya']
fruit_list2=fruit_list1
fruit_list3=fruit_list1[:]

fruit_list2[0]='guva'
fruit_list3[1]='kiwi'

sum=0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0]=='guva':
        sum+=1
    if ls[1]=='kiwi':
        sum+=20

print(sum)
