import pandas

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
data=pandas.read_csv(weather_file_path)
list_data=data["temp"].to_list()
avg=sum(list_data)/len(data["temp"])
print(avg) #output 17.428571428571427

#this is how we normaly calculate the avg but,there is a easy method in pandas
#ie,

print(data["temp"].mean()) #output 17.428571428571427
#to find max from temperature
print(data["temp"].max()) #output 24 

#also we can print temp like this
print(data.temp)
#output
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
print(data.condition)
#output
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny