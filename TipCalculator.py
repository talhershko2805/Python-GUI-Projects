from tkinter import *

root = Tk()

root.title("Tip Calculator")
root.geometry("400x200")

def calculate():
    try:
        total_bill = float(total_bill_entry.get())
        tip = float(tip_entry.get())
        num_of_people = float(num_of_people_entry.get())
        bill_per_person = (total_bill * (1+(tip/100))) / num_of_people
        hidden_bill_label.config(text=f"{bill_per_person:.2f}")
        total_bill_entry.delete(0, END)
        tip_entry.delete(0, END)
        num_of_people_entry.delete(0, END)
    except ValueError:
        total_bill_entry.delete(0, END)
        tip_entry.delete(0, END)
        num_of_people_entry.delete(0, END)
        hidden_bill_label.config(text="Please enter numbers only!")
    except ZeroDivisionError:
        total_bill_entry.delete(0, END)
        tip_entry.delete(0, END)
        num_of_people_entry.delete(0, END)
        hidden_bill_label.config(text="Can't divide by zero people!")

# Labels
total_bill_label = Label(root, text="Total Bill")
total_bill_label.grid(column=0, row=0)
tip_label = Label(root, text="Tip in %")
tip_label.grid(column=0, row=1)
num_of_people_label = Label(root, text="Number of people splitting the bill")
num_of_people_label.grid(column=0, row=2)
final_bill_label = Label(root, text="Final Bill Per Person:")
final_bill_label.grid(column=0, row=4)
hidden_bill_label = Label(root, text="")
hidden_bill_label.grid(column=1, row=4)

# Entries
total_bill_entry = Entry(root)
total_bill_entry.grid(column=1, row=0)
tip_entry = Entry(root)
tip_entry.grid(column=1, row=1)
num_of_people_entry = Entry(root)
num_of_people_entry.grid(column=1, row=2)


# Buttons
calculate_button_label = Button(root, text="Calculate Bill", command=calculate)
calculate_button_label.grid(column=1, row=3)

root.mainloop()