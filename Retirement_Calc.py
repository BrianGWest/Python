from tkinter import *

master = Tk()

# Input labels
Label(master, text="Current Age").grid(row=0)
Label(master, text="Retirement Age").grid(row=1)
Label(master, text="Current Savings").grid(row=2)
Label(master, text="Yearly Contribution").grid(row=3)
Label(master, text="Average Annual Return").grid(row=4)

# Input entries
age = Entry(master)
retire_age = Entry(master)
current_sav = Entry(master)
contribution = Entry(master)
average_ann_return = Entry(master)

# Input grid
age.grid(row=0, column=1)
retire_age.grid(row=1, column=1)
current_sav.grid(row=2, column=1)
contribution.grid(row=3, column=1)
average_ann_return.grid(row=4, column=1)
average_ann_return.insert(0, 0.07)

# Output labels
Label(master, text="Years until retirement").grid(row=6)
Label(master, text="Savings at Retirement").grid(row=7)

# Output entries
years = Entry(master)
retire_sav = Entry(master)

# Output grid
years.grid(row=6, column=1)
retire_sav.grid(row=7, column=1)


def calc_retirement():
    years.delete(0, END)
    retire_sav.delete(0, END)

    years_until_retirement = int(retire_age.get()) - int(age.get())
    years.insert(0, years_until_retirement)

    savings = float(current_sav.get()) * (
        (1 + float(average_ann_return.get())) ** years_until_retirement
    )

    while years_until_retirement > 0:
        years_until_retirement -= 1
        savings += float(contribution.get()) * (
            (1 + float(average_ann_return.get())) ** years_until_retirement
        )
    retire_sav.insert(0, "{:,}".format(int(savings)))


def clear_all():
    age.delete(0, END)
    retire_age.delete(0, END)
    current_sav.delete(0, END)
    contribution.delete(0, END)
    average_ann_return.delete(0, END)

    years.delete(0, END)
    retire_sav.delete(0, END)


button = Button(master, text="Calculate", fg="blue", command=calc_retirement)
button.grid(row=5, column=1, pady=4)

button2 = Button(master, text="Clear All", fg="blue", command=clear_all)
button2.grid(row=8, column=1, pady=4)

mainloop()
