import pandas

weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
data=pandas.read_csv(weather_file_path)
list_data=data["temp"].to_list()
avg=sum(list_data)/len(data["temp"])
print(avg)