# coding: utf-8

from tkinter import Entry, Label, StringVar, Tk , Button

root = Tk()
root.title('Annuaire')

ids = ["name", "last_name", "phone", "adress", "city"]
bouton = ["chercher", "inserer", "effacer"]

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

i, j = 0, 0

for idi in ids:
    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.grid(row=i,column=0)

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.grid(row=i,column=1)

    i += 1

for idi in bouton:
    button = Button(root, text = idi)
    widgets_button[idi] = button
    button.grid(row=i+1,column=j)

    j += 1


root.mainloop()