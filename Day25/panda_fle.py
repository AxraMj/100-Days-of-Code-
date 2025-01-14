# weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
# with open(weather_file_path) as weather_file:
#     content_data=csv.reader(weather_file)
#     print(content_data) #output <_csv.reader object at 0x000002B0DA86EBC0>
#     for row in content_data:
#         print(row)
# This much code to write to get this output--------------------------
# #output
# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny']
# ['Tuesday', '14', 'Rain']
# ['Wednesday', '15', 'Rain']
# ['Thursday', '14', 'Cloudy']
# ['Friday', '21', 'Sunny']
# ['Saturday', '22', 'Sunny']
# ['Sunday', '24', 'Sunny']


import pandas

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
data=pandas.read_csv(weather_file_path)
print(data)
#output
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny