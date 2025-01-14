PLACEHOLDER="[name]"
name_text_path="C:/Users/HP/100-Days-of-Code-/Day24/Mail Merging/Input/Names/invited_names.txt"
with open(name_text_path) as name_file:
    names=name_file.readlines()

mial_txt_path="C:/Users/HP/100-Days-of-Code-/Day24/Mail Merging/Input/Letters/starting_letter.txt"
with open(mial_txt_path) as letter_file:
    content=letter_file.read()
    for name in names:
        striped_name=name.strip()
        x=content.replace(PLACEHOLDER,striped_name)
        output_path=f"C:/Users/HP/100-Days-of-Code-/sample/email/Output/{striped_name}.txt"
        with open(output_path,mode="w") as completed_mail:
            completed_mail.write(x)
    
