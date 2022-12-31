
from tkinter import *
from tkinter import messagebox
import random
from random import randint,choice
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters_list = [random.choice(letters) for _ in range(randint(8, 10))]

    symbols_list = [random.choice(symbols) for _ in range(randint(2, 4))]


    numbers_list = [random.choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)


    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def delete():
    website_entry.delete(0,END)
    password_entry.delete(0,END)

def save():
    website = website_entry.get()
    email = emailorusername_entry.get()
    password = password_entry.get()
    new_data = {
        website:
                    {
                        "email":email,
                        "password":password
                    }
                }

    if len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title='warning',message="please don't leave any boxes empty")

    else:
         is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are details entered \nemail:{email}\npassowrd:{password}\nIs it okay to proceeed?")
         if is_ok :
             try:
                 with open("data.json","r") as data_file:
                     data = json.load(data_file)

             except FileNotFoundError:
                 with open("data.json","w") as data_file:
                     json.dump(new_data,data_file,indent=4)

             else:
                 new_data = data.update(new_data)
                 with open("data.json", mode='w') as data_file:
                        json.dump(new_data,data_file,indent=4)
             finally:
                 delete()


def search():
    current_website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            password = data[current_website]["password"]
            email = data[current_website]["email"]
    except KeyError:
        messagebox.showerror(title="Error", message=f"No data found for {current_website}")

    else:
        messagebox.showinfo(title=f"{current_website}", message=f"Password: {password}\nEmail: {email}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file ="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#labels

website_label = Label()
website_label.config(text="Website: ",font=('Courier',10))
website_label.grid(column=0,row=1)


EmailorUsername_label = Label()
EmailorUsername_label.config(text="Email/Username:",font=('Courier',10))
EmailorUsername_label.grid(column=0,row=2)

password_label = Label()
password_label.config(text="Password:",font=('Courier',10))
password_label.grid(column=0,row=3)

#entries
website_entry = Entry(width=21)
website_entry.grid(column=1,row=1, columnspan=2,sticky='w')
website_entry.focus()

emailorusername_entry = Entry(width=35)
emailorusername_entry.grid(column=1,row=2, columnspan=2,sticky='w')
emailorusername_entry.insert(0,"1234@gmmail.com")


password_entry = Entry(width=21)
password_entry.grid(column=1,row=3, columnspan=1,sticky='w')

#buttons

add_button = Button(width=36)
add_button.config(text="Add",command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky='w')

generate_button = Button(width=14)
generate_button.config(text="Generate password",command=generate_password)
generate_button.grid(column=2,row=3,sticky='w')

search_button = Button(width=14)
search_button.config(text="search",command=search)
search_button.grid(column=2,row=1,sticky='w')

window.mainloop()