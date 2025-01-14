import csv

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
with open(weather_file_path) as weather_file:
    content_data=csv.reader(weather_file)
    temperature = []
    for row in content_data:
        if (row[1]!="temp"):
            temperature.append(int(row[1]))
    print(temperature)
#what if we have lakhs of lakhs of data to handle this method will be more difficult
#so to handle that difficulty we need to use pandas

#to perform data analyss on lots of tabular datas we use panda library
