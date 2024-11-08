from tkinter import *
from tkinter import messagebox
import random
import pyperclip as clip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    random_password = []
    no_letter = random.randint(4,10)
    no_numbers = random.randint(3,5)
    no_symbols = random.randint(2,4)
    for _ in range(no_letter):
        random_password.append(random.choice(letters))
    for _ in range(no_numbers):
        random_password.append(random.choice(numbers))
    for _ in range(no_symbols):
        random_password.append(random.choice(symbols))
    random.shuffle(random_password)
    password_string = ''.join(random_password)
    passw_entry.delete(0,END)
    passw_entry.insert(0,password_string)
    clip.copy(password_string)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    email_id = email_entry.get()
    password = passw_entry.get()

    if len(website_name) == 0 or len(email_id) ==0 or len(password) == 0:
        messagebox.showerror(title="Password Manager", message="All fields are mandatory")
    else:
        message = messagebox.askokcancel(title="Password Manager", message=f"Do you want to save the details "
                                                                       f"->\nWebsite: {website_name}\nEmail ID: "
                                                                       f"{email_id}\nPassword: {password}")
        if message:
            with open("password.txt",mode='a') as f:
                f.write(website_name+" | "+email_id+" | "+password+"\n")
        else:
            messagebox.showinfo(title="Password Manager",message="Info cleared")
        website_entry.delete(0,END)
        passw_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=400,height=300)
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120,100,image=lock_img)
canvas.grid(column=1,row=0)

email = Label(text="Email/Username:")
website = Label(text="Website:")
passw = Label(text="Password:")
email.grid(column=0,row=2)
website.grid(column=0,row=1)
passw.grid(column=0,row=3)

website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0,"hkrishnatre@gmail.com")
passw_entry = Entry(width=30)
website_entry.grid(column=1,row=1, columnspan=2,sticky='ew')
email_entry.grid(column=1,row=2,columnspan=2,sticky='ew')
passw_entry.grid(column=1,row=3,sticky='ew')

generate_passw = Button(text="Generate Password",padx=0,pady=0,command=password_generator)
generate_passw.grid(column=2,row=3,sticky='ew')

add_entry = Button(text="Add",width=45,command=save_password)
add_entry.grid(column=1,row=4,columnspan=2)


window.mainloop()