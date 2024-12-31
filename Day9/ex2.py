travel_log=[
    {
        "Country":"Italy",
        "Visited_places":["Rome","Venice","Florence"]
    },
    {
        "Country":"Japan",
        "Visited_places":["Tokyo","Kyoto","Osaka"]
    }
]

#adding new country
def add_new_country(country_visited,city_visited):
    new_country={}
    new_country["Country"]=country_visited
    new_country["Visited_places"]=city_visited
    travel_log.append(new_country)

add_new_country("russia",["hdskj","jms"])
print(travel_log)