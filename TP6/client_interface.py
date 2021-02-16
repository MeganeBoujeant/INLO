#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""


from tkinter import Tk, Label, StringVar, Entry, Button, messagebox
from tkinter.ttk import Combobox
from individu import Individu


class window(Tk):
    """ Class of Graphical Interface for user which would consult the phone
    book """

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x200')
        self.title("Annuaire")

        self.label_list = ['name', 'last_name', 'phone', 'adress', 'city']
        self.button = ["search", "insert", "erase"]

        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.dict_record = {}

        self.main_page()

    def main_page(self):
        i, j = 0, 0

        for element in self.label_list:

            label = Label(self, text=element)
            self.widgets_labs[element] = label
            label.grid(row=i, column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            self.widgets_entry[element] = entry
            entry.grid(row=i, column=1)

            i += 1

        for idi in self.button:
            button = Button(self, text=idi)
            self.widgets_button[idi] = button
            button.grid(row=i + 1, column=j)

            j += 1

        self.widgets_button['insert'].config(command=self.get_fields())
        self.widgets_button['search'].config(command=self.search())

    def get_fields(self):
        i = Individu(self.widgets_entry['name'].get(),
                     self.widgets_entry['last_name'].get(),
                     self.widgets_entry['phone'].get(),
                     self.widgets_entry['adress'].get(),
                     self.widgets_entry['city'].get())
        self.dict_record[self.widgets_entry['name'].get()] = i
        print(self.dict_record)

    def search(self):
        search_name = self.widgets_entry['name'].get()

        if search_name:
            k = 0
            list_of_results = []
            for key, value in self.dict_record.items():
                if key == search_name:
                    k += 1
                    list_of_results.append(value)
            if k == 0:
                messagebox.showinfo(title="No result !",
                                    message="No name correspond to your \
                                    research.")
            else:
                results = Combobox(self, values=list_of_results)
                results.pack()
        else:
            messagebox.showinfo(title="Warning !", message="Please, enter name \
                                to make a reserch of record.")


if __name__ == '__main__':
    app = window()
    app.mainloop()
