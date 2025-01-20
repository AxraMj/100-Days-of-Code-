from tkinter import *
from tkinter import messagebox #meassage box is not class
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Opps!!", message="Fill all the field")
    else:
        #create a message box
        # messagebox.showinfo(title="title",message="Message")
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\n password: {password}\n is it ok to save?")
        if is_ok:
            file_path="Day29/002 password-manager-start/data.txt"
            with open(file_path,"a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
  


# ---------------------------- UI SETUP ------------------------------- #

# Initialize window
windows = Tk()
windows.title("Password Generator")
windows.config(padx=20, pady=20)

# Display image
canvas = Canvas(width=200, height=200)
image_path = PhotoImage(file="E:/100 Days Python/100-Days-of-Code-/Day29/002 password-manager-start/logo.png")
canvas.create_image(100, 100, image=image_path)
canvas.grid(column=1, row=0)

# Website Label and Entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
# Email/Username Label and Entry
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ajm24@gmail.com")
# Password Label and Entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)  # Consistent width
password_entry.grid(row=3, column=1)

generate_button= Button(text="Generate Password")
generate_button.grid(row=3,column=2)

Add_button= Button(text="Add",width=36,command=save)
Add_button.grid(row=4,column=1,columnspan=2)
# Run the application
windows.mainloop()
