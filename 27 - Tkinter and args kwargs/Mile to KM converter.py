from tkinter import *

km = 1.60934


def calculate():
    a_label.config(text=round(float(miles_input.get()) * km, 4))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=320, height=150)
window.config(padx=20, pady=20)

# Miles label
m_label = Label(text="Miles", font=("Arial", 12))
m_label.grid(column=2, row=0)
m_label.config(pady=10, padx=10)

# KM label
km_label = Label(text="KM", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config(pady=10, padx=10)

# is equal to label
iet_label = Label(text="is equal to", font=("Arial", 12))
iet_label.grid(column=0, row=1)
iet_label.config(pady=10, padx=10)

# answer label
a_label = Label(text="0", font=("Arial", 12))
a_label.grid(column=1, row=1)
a_label.config(pady=10, padx=10)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
