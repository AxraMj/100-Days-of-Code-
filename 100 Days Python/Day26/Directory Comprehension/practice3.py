
wether_F={
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}
#syntax result={new_key:new_value for item in sentence}
result={key:value*9/5 +32 for (key,value) in wether_F.items()}
print(result)