"""
A program that stores book information:
Title, Author,
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *

window = Tk()

# Form fields
# Title field
title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)
title_value = Entry(window, textvariable=StringVar())
title_value.grid(row=0, column=1)

# Author Field
author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)
author_value = Entry(window, textvariable=StringVar())
author_value.grid(row=0, column=3)

# Year field
year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)
year_value = Entry(window, textvariable=StringVar())
year_value.grid(row=1, column=1)

#ISBN field
isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)
isbn_value = Entry(window, textvariable=StringVar())
isbn_value.grid(row=1, column=3)

# Buttons
view_all_btn = Button(window, text="View all", width=12)
view_all_btn.grid(row=2, column=3)
search_entry_btn = Button(window, text="Search entry", width=12)
search_entry_btn.grid(row=3, column=3)
add_entry_btn = Button(window, text="Add Entry", width=12)
add_entry_btn.grid(row=4, column=3)
update_btn = Button(window, text="Update", width=12)
update_btn.grid(row=5, column=3)
delete_btn = Button(window, text="Delete", width=12)
delete_btn.grid(row=6, column=3)
close_btn = Button(window, text="Close", width=12)
close_btn.grid(row=7, column=3)

listbox = Text(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

window.mainloop()
