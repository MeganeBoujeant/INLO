#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""


from tkinter import *
from individu import Individu


class window(Tk):
    """ Class of Graphical Interface for user which would consult the phone
    book """

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x200')
        self.title("Annuaire")
        self.main_page()

    def main_page(self):
        """ """
        label_list = ['name', 'last name', 'phone', 'adress', 'city']
        button = ["search", "insert", "erase"]

        widgets_labs = {}
        widgets_entry = {}
        widgets_button = {}

        i, j = 0, 0

        for element in label_list:

            label = Label(self, text=element)
            widgets_labs[element] = label
            label.grid(row=i, column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            widgets_entry[element] = entry
            entry.grid(row=i, column=1)

            i += 1

        for idi in button:
            button = Button(self, text=idi)
            widgets_button[idi] = button
            button.grid(row=i + 1, column=j)

            j += 1

        widgets_button['insert'].config(command=lambda: self.get_fields(widgets_entry))

    def get_fields(self, widgets_entry):
        dico = {}
        i = Individu(widgets_entry['name'].get(), widgets_entry['last_name'].get(), widgets_entry['phone'].get(), widgets_entry['adress'].get(), widgets_entry['city'].get())
        dico[widgets_entry['name'].get()] = i
        print(i)


if __name__ == '__main__':
    app = window()
    app.mainloop()
