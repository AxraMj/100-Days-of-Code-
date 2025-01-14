# weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
# with open(weather_file_path) as weather_file:
#     content=weather_file.readlines()
#     print(content)

#output:['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
#this will be very difficult to proceess so we use an library called csv

import csv

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
with open(weather_file_path) as weather_file:
    content_data=csv.reader(weather_file)
    print(content_data) #output <_csv.reader object at 0x000002B0DA86EBC0>
    for row in content_data:
        print(row)
#output
# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny']
# ['Tuesday', '14', 'Rain']
# ['Wednesday', '15', 'Rain']
# ['Thursday', '14', 'Cloudy']
# ['Friday', '21', 'Sunny']
# ['Saturday', '22', 'Sunny']
# ['Sunday', '24', 'Sunny']