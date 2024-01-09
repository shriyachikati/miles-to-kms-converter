from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30)

user_input = Entry(width=12)
user_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

text2_label = Label(text="is equal to")
text2_label.grid(row=1, column=0)

output_label = Label(text="", width=12)
output_label.grid(row=1, column=1)

text3_label = Label(text="Km")
text3_label.grid(row=1, column=2)

miles = 0
def get_input():
    miles = float(user_input.get())
    kms = miles * 1.609
    output_label["text"] = str(round(kms, 4))


button = Button(text="Calculate", command=get_input)
button.grid(row=2, column=1)

window.mainloop()