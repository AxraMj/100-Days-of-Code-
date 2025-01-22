#Type Error, Type Checking and Type Conversion


            # char_len=print(len(input("What is your name?")))
            # print("Your Name has" +char_len+ "characters.")

# TypeError: can only concatenate str (not "NoneType") to str

#convert to staring to concatenate
char_len=str(len(input("What is your name?")))
print("Your Name has " +char_len+ " characters.")

print()

a=10
print("You have " +str(a)+ " marks")

print()

print(70 + float("10.5"))
print(int("456") + float("56.7"))