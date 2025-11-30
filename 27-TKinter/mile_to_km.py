import tkinter as tk


def miles_to_km():
    inserted_mile = float(miles_input.get())
    km = round(inserted_mile * 1.609)
    km_output.config(text=km)


window = tk.Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# input box
miles_input = tk.Entry()
miles_input.grid(column=1, row=0)


# Miles label
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)


# equal label
equal_label = tk.Label(text="Is equal to")
equal_label.grid(column=0, row=2)


# km output
km_output = tk.Label(text="0")
km_output.grid(column=1, row=1)


# km label
km_label = tk.Label(text="KM")
km_label.grid(column=2, row=1)


# button
button = tk.Button(text="calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
