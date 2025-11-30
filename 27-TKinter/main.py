from tkinter import *
from turtle import color


def button_clicked():
    input_text = my_input.get()
    my_label.config(text=input_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# label
my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label['text'] = "hamed label"
my_label.config(text="New label")
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# input
my_input = Entry(width=20)
my_input.grid(column=3, row=2)


# new button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

window.mainloop()
