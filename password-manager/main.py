from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip as clip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    """This function generates a random password for the website"""
    password_letter = [choice(letters) for _ in range(randint(6,10))]
    password_number = [choice(numbers) for _ in range(randint(3,5))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]
    random_password = password_letter + password_number + password_symbol
    shuffle(random_password)
    password_string = ''.join(random_password)
    passw_entry.delete(0,END)
    passw_entry.insert(0,password_string)
    clip.copy(password_string)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """This function is used to save the data entered by user into .json format"""
    website_name = website_entry.get()
    email_id = email_entry.get()
    password = passw_entry.get()

    new_data = {
        website_name: {
            "email": email_id,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(email_id) == 0 or len(password) == 0:
        messagebox.showerror(title="Password Manager", message="All fields are mandatory")
    else:
        try:
            with open("password.json", 'r') as data_file:
                con = messagebox.askokcancel(title="Confirm Entry",message=f"Do you want to save the following data:\nWebsite: {website_name}\nEmail ID: {email_id}\nPassword: {password}")
                if con:
                    #loading the json file
                    data = json.load(data_file)
                else:
                    return -1
        except FileNotFoundError:
            with open("password.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update old data with new data
            data.update(new_data)

            with open("password.json",'w') as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            #remove all the saved data from the GUI
            website_entry.delete(0, END)
            passw_entry.delete(0, END)

# ----------------------------SEARCHING PASSWORD----------------------- #
def search_password():
    """Search password from the created .json Database"""
    website_name = website_entry.get()
    try:
        with open("password.json",'r') as data_file:
            data = json.load(data_file)
            if website_name in data.keys():
                messagebox.showinfo(title="Search Result",message=f"Website: {website_name}\nEmail ID: {data[website_name]["email"]}\nPassword: {data[website_name]["password"]}")
            else:
                raise KeyError
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Database file present")
    except KeyError:
        messagebox.showerror(title="Not Found",message="Entered Website is not in Database")
# ---------------------------- UI SETUP ------------------------------- #

#create the window
window = Tk()
window.title("Password Manager")
window.minsize(width=400,height=300)
window.config(padx=50,pady=50)

#create canvas for placing the tokens
canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120,100,image=lock_img)
canvas.grid(column=1,row=0)

#create all the label
email_label = Label(text="Email/Username:")
website_label = Label(text="Website:")
passw_label = Label(text="Password:")

#place all labels on the canvas
email_label.grid(column=0,row=2)
website_label.grid(column=0,row=1)
passw_label.grid(column=0,row=3)

#create all textboxes for user input
website_entry = Entry(width=30)
website_entry.focus()#cursor initial location will be at this input
email_entry = Entry(width=35)
email_entry.insert(0,"hkrishnatre@gmail.com")#Default Email for Ease of access
passw_entry = Entry(width=30)

#placing all the textboxes in the canvas
website_entry.grid(column=1,row=1,sticky='ew')
email_entry.grid(column=1,row=2,columnspan=2,sticky='ew')
passw_entry.grid(column=1,row=3,sticky='ew')

#creating button for searching passwrd for website
search_passw = Button(text="Search",padx=0,pady=0,command=search_password)
search_passw.grid(column=2,row=1,sticky='ew')

#creating button for generating random password
generate_passw = Button(text="Generate Password",padx=0,pady=0,command=password_generator)
generate_passw.grid(column=2,row=3,sticky='ew')

#creating button for add all the user input to database
add_entry = Button(text="Add",width=45,command=save_password)
add_entry.grid(column=1,row=4,columnspan=2)


window.mainloop()