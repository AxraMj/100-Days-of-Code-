#nesting
#dictionary_item={
#   key=[list],
#   key2={dic}
#}

#nest:List in a dictionary
class_students={
    "name":["Akshara","Avinash","Aiswarya","Akash"],
    "Department":"MCA",
}



#nest:dictionary in dictionary
student_age={
    "Akshara":24,
    "Avinash":20,
    "Aiswarya":18,
    "Akash":26
}
class_students={
    "name":["Akshara","Avinash","Aiswarya","Akash"],
    "Department":"MCA",
    "age":{"student_age":[20,30,40,50]}
}

print(class_students["age"])


#nesting dictionary inside a list
# [
#     {
#         key:[list],
#         key2:{dic}
#     },
#     {
#         key:[list],
#         key2:{dic}
#     },
#     {
#         key:[list],
#         key2:{dic}
#     },
# ]

student_dic=[
    {
        "class1":{"students":["Akash","Avinash"]},
        "Department":"MCA",
    },
    {
        "class2":{"Students":["Akshara","Aiswarya"]},
        "Department":"BCA"
    },
]

