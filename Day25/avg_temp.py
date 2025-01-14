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