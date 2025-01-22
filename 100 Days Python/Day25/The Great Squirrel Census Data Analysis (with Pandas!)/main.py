import pandas

path="C:/Users/HP/100-Days-of-Code-/Day25/The Great Squirrel Census Data Analysis (with Pandas!)/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"
data=pandas.read_csv(path)

list_color = data["Primary Fur Color"].to_list()
gray=list_color.count("Gray")
Cinnamon=list_color.count("Cinnamon")
black=list_color.count("Black")
print(gray,Cinnamon,black)


data = [
    {"id": 1, "fur_color": "gray", "count": gray},
    {"id": 2, "fur_color": "Cinnamon", "count": Cinnamon},
    {"id": 3, "fur_color": "black", "count": black},
]

datas=pandas.DataFrame(data)
print(datas)

path="C:/Users/HP/100-Days-of-Code-/Day25/The Great Squirrel Census Data Analysis (with Pandas!)/squirrel_color.csv"
datas.to_csv(path)