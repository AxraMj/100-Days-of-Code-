#  F = (C * 9/5) + 32 quation

import pandas

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
data=pandas.read_csv(weather_file_path)

f=(data.temp * (9/5) ) +32
print(f)

#converting only monday condition temp to fahrenhite
monday=data[data.day == "Monday"]
print(monday.temp * (9/5)  +32)
#output 
# 0    53.6

