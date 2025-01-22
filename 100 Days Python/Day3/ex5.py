#Love Calculator
#💪 This is a Difficult Challenge 💪
#Instructions
#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs.
#Then check for the number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.
#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."
#e.g.
#name1 = "Angela Yu"
#name2 = "Jack Bauer"
#T occurs 0 times
#R occurs 1 time
#U occurs 2 times
#E occurs 2 times
#Total = 5
#L occurs 1 time
#O occurs 0 times
#V occurs 0 times
#E occurs 2 times
#Total = 3
#Love Score = 53
#Print: "Your score is 53."


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
