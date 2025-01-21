#Find Number of days above Average Temperature



days_temp=int(input("How many day's temperature? "))
total=0
temp=[]
for i in range(days_temp):
    days=int(input(f"day {i}'s high temp: "))
    temp.append(days)
    total+=temp[i]

avg= round(total/days_temp)
print(f"Average= {avg}")

above=0
for i in temp:
    if i>above:
        above+=1

print(f"{above} days above average")

    