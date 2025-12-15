from tkinter import *

root = Tk()

# General
root.title("To-Do List App")
root.geometry("400x300")

def add_task():
    task = enter_task_entry.get()
    if len(task) == 0:
        status_label.config(text="Please enter a task")
    else:
        task_listbox.insert(END, task)
        enter_task_entry.delete(0, END)
        status_label.config(text="")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if len(selected_task_index) == 0:
        status_label.config(text="No tasks selected")
    else:
        task_listbox.delete(selected_task_index[0])

def save_tasks():
    tasks = task_listbox.get(0, END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    status_label.config(text="Tasks saved")

def load_tasks():
    try:
        task_listbox.delete(0, END)

        with open ("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                if task: # Skip empty lines
                    task_listbox.insert(END, task)
        status_label.config(text="Tasks loaded")

    except FileNotFoundError:
        status_label.config(text="No saved tasks file found")


# Labels
enter_task_label = Label(root, text="Enter a task:")
enter_task_label.grid(column=0, row=0)
status_label = Label(root, text="")
status_label.grid(column=0, row=6)

# Entries
enter_task_entry = Entry(root)
enter_task_entry.grid(column=1, row=0)

# Buttons
enter_task_button = Button(root, text="Add task", command=add_task)
enter_task_button.grid(column=2, row=0)
delete_task_button = Button(root, text="Delete selected task", command=delete_task)
delete_task_button.grid(column=0, row=2)
save_tasks_button = Button(root, text="Save Tasks to File", command=save_tasks)
save_tasks_button.grid(column=1, row=2)
load_tasks_button = Button(root, text="Load Tasks from File", command=load_tasks)
load_tasks_button.grid(column=2, row=2)

# Listbox
task_listbox = Listbox(root)
task_listbox.grid(column=0, row=1, columnspan=3)


root.mainloop()