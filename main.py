from tkinter import *
from tkinter.font import Font
from backend import Database

db = Database()

def clear_widget(widget):
    widget.delete(0, END)


def update_widget(widget, value):
    clear_widget(widget)
    widget.insert(END, value)


def read_values():
    title = title_value.get()
    author = author_value.get()
    year = year_value.get()
    isbn = isbn_value.get()
    return title, author, year, isbn


def update_values(item_tuple):
    update_widget(title_value, item_tuple[1])
    update_widget(author_value, item_tuple[2])
    update_widget(year_value, item_tuple[3])
    update_widget(isbn_value, item_tuple[4])


def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = eval(listbox.get(index))
        update_values(selected_tuple)
    except IndexError:
        pass


def get_id():
    return selected_tuple[0]


def view_command():
    clear_widget(listbox)
    for row in db.view():
        listbox.insert(END, str(row)[1:-1] + "\n")


def search_command():
    clear_widget(listbox)
    title, author, year, isbn = read_values()
    search_result = db.search(title, author, year, isbn)
    if search_result:
        for row in search_result:
            listbox.insert(END, str(row)[1:-1] + "\n")
    else:
        listbox.insert(END, "Entries not found")


def add_command():
    title, author, year, isbn = read_values()
    db.insert(title, author, year, isbn)
    update_widget(listbox, "Entry added")


def delete_command():
    db.delete(get_id())
    view_command()


def update_command():
    title, author, year, isbn = read_values()
    item_id = get_id()
    db.update(item_id, title, author, year, isbn)
    view_command()

window = Tk()
window.wm_title("BookShelf")

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

# ISBN field
isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)
isbn_value = Entry(window, textvariable=StringVar())
isbn_value.grid(row=1, column=3)

# Buttons
view_all_btn = Button(window, text="View all", width=12, command=view_command)
view_all_btn.grid(row=2, column=3)
search_entry_btn = Button(
    window, text="Search entry", width=12, command=search_command)
search_entry_btn.grid(row=3, column=3)
add_entry_btn = Button(window, text="Add Entry", width=12, command=add_command)
add_entry_btn.grid(row=4, column=3)
update_btn = Button(window, text="Update", width=12, command=update_command)
update_btn.grid(row=5, column=3)
delete_btn = Button(window, text="Delete", width=12, command=delete_command)
delete_btn.grid(row=6, column=3)
close_btn = Button(window, text="Close", width=12, command=window.destroy)
close_btn.grid(row=7, column=3)

myFont = Font(family="Times New Roman", size=10)
listbox = Listbox(window, height=6, width=35, state="normal")
listbox.configure(font=myFont)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
listbox.bind('<<ListboxSelect>>', get_selected_row)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

window.mainloop()
