from tkinter import *

root = Tk()
root.title("Smart Shopping List App")
root.geometry("400x300")

def add():
    user_item = input_entry.get()
    if user_item == "":
        status_label.config(text="Please enter an item!")
        return
    user_item = user_item[0].upper() + user_item[1:].lower()
    all_items = shopping_list.get(0, END)
    if user_item in all_items:
        status_label.config(text="Item already exists!")
        input_entry.delete(0, END)
    else:
        shopping_list.insert(END, user_item)
        input_entry.delete(0, END)
        status_label.config(text="Number of items: " + str(len(shopping_list.get(0, END))))


def remove():
    item_selected = shopping_list.curselection()
    if item_selected:
        shopping_list.delete(item_selected[0])
    status_label.config(text="Number of items: " + str(len(shopping_list.get(0, END))))


def clear():
    shopping_list.delete(0, END)
    status_label.config(text="Number of items: " + str(len(shopping_list.get(0, END))))



# Labels
input_label = Label(root, text="Enter a new item:")
input_label.grid(column=0, row=0)
status_label = Label(root, text="")
status_label.grid(column=0, row=3)

# Entries
input_entry = Entry(root)
input_entry.grid(column=1, row=0)

# Buttons
add_input_button = Button(root, text="Add", command=add)
add_input_button.grid(column=2, row=0, padx=10, pady=10)
remove_button = Button(root, text="Remove", command=remove)
remove_button.grid(column=0, row=2, padx=10, pady=10)
clear_button = Button(root, text="Clear List", command=clear)
clear_button.grid(column=1, row=2, padx=10, pady=10)

# Listbox
shopping_list = Listbox(root, height=10, width=40)
shopping_list.grid(column=1, row=1, columnspan=3)

root.mainloop()