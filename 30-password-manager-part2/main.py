
import json
import tkinter as tk
from tkinter import messagebox
from random import choices, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!#$%&()*+"
    pas_len = randint(12, 14)
    password = "".join(choices(chars, k=pas_len))
    password_input.delete(0, tk.END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get Entries data
    website = website_input.get().lower()
    e_u = e_u_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email/username": e_u,
            "password": password
        }
    }

    # Validate data
    if not website or not e_u or not password:
        messagebox.showerror(title="Oops",
                             message="Please don't leave any fields empty!")
        return

    # ask user for confirmation
    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered: \nEmail/username: {e_u} \nPassword: {password}")
    if not is_ok:
        return
    try:
        # Save data in text
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", mode="w") as data_file:
            json.dump(new_data, data_file, indent=2)
    else:
        data.update(new_data)
        with open("data.json", mode="w",)as data_file:
            json.dump(data, data_file, indent=2)
    finally:
        # Clear entries
        website_input.delete(0, tk.END)
        password_input.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get().lower()
    if not website:
        return

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", mode="w") as data_file:
            json.dump({}, data_file)
        messagebox.showinfo(
            title="Empty data base", message=f"There is no data to found")
    else:
        website_data = data.get(website, None)
        if website_data == None:
            messagebox.showinfo(
                title=website, message=f"No details for {website} exists.")
        else:
            messagebox.showinfo(
                title=website, message=f"Email/username: {website_data['email/username']}\n password: {website_data['password']}")
            pyperclip.copy(website_data['password'])


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = tk.PhotoImage(file="./logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:", font=("Arial", 16, "normal"))
website_label.grid(column=0, row=1)

website_input = tk.Entry(width=35)
website_input.grid(column=1, row=1,
                   )
website_input.focus()

search_button = tk.Button(text="Search", width=21, command=find_password)
search_button.grid(column=3, row=1)

e_u_label = tk.Label(
    text="Email/Username:", font=("Arial", 16, "normal"))
e_u_label.grid(column=0, row=2)

e_u_input = tk.Entry(width=35)
e_u_input.grid(column=1, row=2, columnspan=2)
e_u_input.insert(0, "email@provider.com")


password_label = tk.Label(text="Password:", font=(
    "Arial", 16, "normal"), )
password_label.grid(column=0, row=3)

password_input = tk.Entry(width=21)
password_input.grid(column=1, row=3)

gen_pass_button = tk.Button(
    text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)


add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
