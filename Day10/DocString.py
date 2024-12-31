#Check leap year and say  number of days in the month

def is_leap_year(year):
    """To check leap year or not""" #docstring:to check
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            return False
        return True
    return False
        
def month_days(year,month):
    days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month==2:
        return 29
    return days_in_month[month-1]

year=int(input("Enter Year: "))
month=int(input("Enter the month:"))
output=month_days(year,month)
print(output)


