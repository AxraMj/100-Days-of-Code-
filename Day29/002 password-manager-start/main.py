from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

# Email/Username Label and Entry
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

# Password Label and Entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)  # Consistent width
password_entry.grid(row=3, column=1)

generate_button= Button(text="Generate Password")
generate_button.grid(row=3,column=2)

Add_button= Button(text="Add",width=36)
Add_button.grid(row=4,column=1,columnspan=2)
# Run the application
windows.mainloop()
