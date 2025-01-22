

file1_path="C:/Users/HP/100-Days-of-Code-/Day26/practice3/file1.txt"
file2_path="C:/Users/HP/100-Days-of-Code-/Day26/practice3/file2.txt"

with open(file1_path) as file_1:
    file_1_content=file_1.readlines()

with open(file2_path) as file_2:
    file_2_content=file_2.readlines()

result=[int(num) for num in file_1_content if num in file_2_content]

PermissionError(result)
