#Find Number of days above Average Temperature



days_temp=int(input("How many day's temperature? "))
total=0
for i in range(1,days_temp+1):
    days=int(input(f"day {i}'s high temp: "))
    total+=days

avg= round(total/days_temp)
print(f"Average= {avg}")
    