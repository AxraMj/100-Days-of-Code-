student_dict={
    "student":["Akshara","Akash","Avinash"],
    "score":[56,76,98]
}

#looping through dictionary
for (key,values) in student_dict.items():
    print(values)

import pandas

student_dataframe=pandas.DataFrame(student_dict)
print(student_dataframe)

#looping through dataframe
for (key,values) in student_dataframe.items():
    print(values)
#panda is having inbuilt loop
#it allow us to loop through each of the row in dataframe otherthan each of the columns
for (index,row) in student_dataframe.iterrows():
    print(row)
    print()
    print(row.score)
    if row=="Akshara":
        print(row.score)