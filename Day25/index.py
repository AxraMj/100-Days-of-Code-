import csv

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
with open(weather_file_path) as weather_file:
    content_data=csv.reader(weather_file)
    temperature = []
    for row in content_data:
        if (row[1]!="temp"):
            temperature.append(int(row[1]))
    print(temperature)