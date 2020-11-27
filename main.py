from tkinter import *

window = Tk()


def km_to_miles():
    try:
        miles = round(float(entry1_value.get()) * 1.6, 2)
    except:
        miles = "Not a number"
    text1.insert(END, miles)

entry0 = Label(window,text="Km to Miles")
entry0.grid(row=0, column=0)

button1 = Button(window, text="Execute", command=km_to_miles)
button1.grid(row=1, column=1)

entry1_value = StringVar()
entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=1, column=0)

text1 = Text(window, height=1, width=15)
text1.grid(row=2, column=0)

window.mainloop()
