import pandas
weather_file_path="C:/Users/HP/100-Days-of-Code-/Day25/002 weather-data.csv"
data=pandas.read_csv(weather_file_path)
print(type(data)) #DataFrame A DataFrame in Python's pandas library which is a whole table in the csv sheet
print(type(data["temp"])) #series , every single column in the csv sheet is a series

#Look various operation in pada documentation(resference)

#to converet data in csv file to dictionary 
dic_data=data.to_dict()
print(dic_data)
#output
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}


#to convert to list
list_data=data["temp"].to_list()
print(list_data)
#output [12, 14, 15, 14, 21, 22, 24]
#find length of list
print(len(list_data)) #output 7