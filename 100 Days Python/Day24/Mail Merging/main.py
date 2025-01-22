#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER="[name]"

file_path="C:/Users/HP/100-Days-of-Code-/Day24/Mail Merging/Input/Names/invited_names.txt"
with open(file_path) as names_file:
    names = names_file.readlines() #change names into list


file_path_letter="C:/Users/HP/100-Days-of-Code-/Day24/Mail Merging/Input/Letters/starting_letter.txt"
with open(file_path_letter) as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name=name.strip() #prper aligig the content we use strip
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        # print(new_letter) #instead of pring lets create a file to print the email
        output_path=f"C:/Users/HP/100-Days-of-Code-/Day24/Mail Merging/Output/ReadyToSend/letter_for{stripped_name}.txt"
        with open(output_path,mode="w") as completed_letter:
            completed_letter.write(new_letter)
