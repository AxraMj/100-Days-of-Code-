import pandas

path="C:/Users/HP/100-Days-of-Code-/Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv"
data=pandas.read_csv(path)


#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter the name:").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)