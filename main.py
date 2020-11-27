from tkinter import *

window=Tk()

button1 = Button(window, text="Execute")
button1.grid(row=0, column=1)

entry1 = Entry(window)
entry1.grid(row=0, column=0)

text1 = Text(window,  height=2, width=20)
text1.grid(row=1, column=0)

window.mainloop()
