#From scrach create a dataframe ie, a table
import pandas
students = {
    "student_1": {
        "name": "Alice",
        "age": 20,
        "grade": "A",
    },
    "student_2": {
        "name": "Bob",
        "age": 22,
        "grade": "B",
    },
    "student_3": {
        "name": "Charlie",
        "age": 19,
        "grade": "A+",
    }
}
 
 #dic to create csv file

data=pandas.DataFrame(students)
print(data)
#output
#       student_1 student_2 student_3
# name      Alice       Bob   Charlie
# age          20        22        19
# grade         A         B        A+


#to create a csv file
path="C:/Users/HP/100-Days-of-Code-/Day25/Dataframe create/Studentdata.csv"
data.to_csv(path)