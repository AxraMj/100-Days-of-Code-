first_name=input("Enter your First name:")
last_name=input("Enter your last name:")

def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"


output=format_name(first_name,last_name)
print(output)