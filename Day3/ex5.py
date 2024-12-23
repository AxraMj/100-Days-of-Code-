print("Welcome to Love Calculator!!")
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

print("Calculating Love Score....")
name1 = name1.lower()
name2 = name2.lower()

both = name1 + name2
print(both)

# Correct use of f-strings with single quotes inside double quotes
print(f"T occurs {both.count('t')} times")
print(f"R occurs {both.count('r')} times")
print(f"U occurs {both.count('u')} times")
print(f"E occurs {both.count('e')} times")
total1 = both.count('t') + both.count('r') + both.count('u') + both.count('e')

print(f"L occurs {both.count('l')} times")
print(f"O occurs {both.count('o')} times")
print(f"V occurs {both.count('v')} times")
print(f"E occurs {both.count('e')} times")
total2 = both.count('l') + both.count('o') + both.count('v') + both.count('e')

# Combine the counts to form the love score
total = int(str(total1) + str(total2))
print(f"Love Score is {total}")

# Provide the appropriate message based on the love score
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 <= total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
