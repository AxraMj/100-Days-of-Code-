import pandas

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
data=pandas.read_csv(weather_file_path)

fetch_row=data[data.day == "Monday"]
print(fetch_row)

#output
#       day  temp condition
# 0  Monday    12     Sunny

#fetch row that is having max temperature
max_temp=data.temp.max()
fetch_max_temp=data[data.temp == max_temp]
print(fetch_max_temp)
#writing the above code in one line is:
# print(data[data.temp == data.temp.max()])
#output 
# day  temp condition
# 6  Sunday    24     Sunny


friday=data[data.day=="Friday"]
print(friday.condition)
#output 
# 4    Sunny