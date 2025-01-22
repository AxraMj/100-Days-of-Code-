print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
percentage_tip=float(input("What percentage tip would you like to give? 10, 12, or 15?"))
split_bill =float(input("How many people to split the bill?")  )
total = (total_bill * (1 + percentage_tip / 100)) / split_bill
print(f"Each person should pay: ${total}")
