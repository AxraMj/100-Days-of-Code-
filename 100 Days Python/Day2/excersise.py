# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have. 
# Create a program using maths and f-Strings that tells us how many days, weeks, 
# months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.    
# Where x, y and z are replaced with the actual calculated numbers.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Try copying the example output into your code and replace the numbers with your own.

# 🚨 Don't change the code below 
age=int(input("Enter your age:"))
year_left=90-age
days_left=year_left*365
weeks_left=year_left*52
months_left=year_left*12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")



