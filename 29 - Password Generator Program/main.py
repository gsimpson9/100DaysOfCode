from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Please enter your email into the code before running
email = 'test@outlook.com'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = ''.join(password_list)
    pw_input.delete(0, END)
    pw_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    user_email = email_input.get()
    pw = pw_input.get()
    new_data = {
        website: {
            'email': user_email,
            'password': pw
        }
    }

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {user_email}"
                                               f"\nPassword: {pw}\nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open('data.json', 'w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
                messagebox.showinfo(title='Saved', message=f"Your credentials for {website}"
                                                           f" have been saved successfully")
            finally:
                website_input.delete(0, END)
                pw_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get().title()
    user_email = email_input.get()
    pw = pw_input.get()
    try:
        with open('data.json', 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title='Login credentials',
                                    message=f"Your login credentials for {website.title()} are:"
                                            f"\nUsername: {data[website]['email']}"
                                            f"\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title='Login credentials',
                                    message=f'There are no login credentials for "{website}"'
                                            f' currently saved.')
    except FileNotFoundError:
        messagebox.showinfo(title='Login credentials',
                            message=f'No data file found.\nPlease submit at least one entry'
                                    f' before searching.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='#F7ECDE')

# Canvas
canvas = Canvas(width=200, height=200, bg='#F7ECDE')
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:", bg='#F7ECDE')
web_label.grid(column=0, row=1, sticky='e')
email_label = Label(text="Email/Username:", bg='#F7ECDE')
email_label.grid(column=0, row=2, sticky='e')
pw_label = Label(text="Password:", bg='#F7ECDE')
pw_label.grid(column=0, row=3, sticky='e')

# Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
email_input = Entry(width=25)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, email)
pw_input = Entry(width=10)
pw_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3, sticky="EW")
search = Button(text="Search", command=find_password)
search.grid(column=2, row=1, sticky="EW")
add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
