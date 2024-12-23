print("Lets find the Leap year!! ")
year=int(input("Enter the a year:"))

if year%4 == 0:
    if year%100==0 and year%400==0 or year%100!=0:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Rule:
# Divisible by 4: The year must be divisible by 4.
# Not Divisible by 100: If the year is divisible by 100, it is not a leap year unless...
# Divisible by 400: The year is also divisible by 400.

# Steps:
# If the year is divisible by 4 and not divisible by 100, it is a leap year.
# If the year is divisible by 400, it is also a leap year (even if it is divisible by 100).

# Example:
# 2000: Divisible by 4, divisible by 100, and divisible by 400 → Leap year.
# 1900: Divisible by 4, divisible by 100, but not divisible by 400 → Not a leap year.
# 2024: Divisible by 4, not divisible by 100 → Leap year.
# 2023: Not divisible by 4 → Not a leap year.
