#PyPassword Generator Project
print("Welcome to PyPassword Generator!")
numbers=int(input("How many numbers do you want in your password? "))
letters=int(input("How many letters do you want in your password? "))
symbols=int(input("How many symbols do you want in your password? "))
import random
password=""

for n in range(0,numbers+1):
    password+=str(random.randint(0,9))
for n in range(0,letters+1):
    password+=random.choice("abcdefghijklmnopqrstuvwxyz")
for n in range(0,symbols+1):
    password+=random.choice("!@#$%^&*()")
print(f"password={password}")
