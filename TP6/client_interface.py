#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""


from tkinter import Tk, Label, StringVar, Entry, Button, messagebox, Listbox
from individu import Individu


class Window(Tk):
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
        """ This method allows to have the main view of the interface. """
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

        self.widgets_button['insert'].config(command=self.get_fields)
        self.widgets_button['search'].config(command=self.search)
        self.widgets_button['erase'].config(command=self.erase)

    def get_fields(self):
        """ This method allows to insert a new individu in the Annuaire. """
        i = Individu(self.widgets_entry['name'].get(),
                     self.widgets_entry['last_name'].get(),
                     self.widgets_entry['phone'].get(),
                     self.widgets_entry['adress'].get(),
                     self.widgets_entry['city'].get())
        self.dict_record[self.widgets_entry['name'].get()] = i

    def search(self):
        """ This method allows to search if a name is in the Annuaire. """
        search_name = self.widgets_entry['name'].get()

        if search_name:
            s_nb = 0
            list_of_results = []
            for key, value in self.dict_record.items():
                if key == search_name:
                    s_nb += 1
                    list_of_results.append(value)
            if s_nb == 0:
                messagebox.showinfo(title="No result !",
                                    message="No name correspond to your \
                                    research.")
            else:
                self.geometry('500x280')
                results = Listbox(self, height=5, width=40,
                                  selectbackground='pink')
                index = 0
                for element in list_of_results:
                    results.insert(index, element)
                    index += 1
                results.grid(row=(len(self.label_list)+2), column=1)
        else:
            messagebox.showwarning(title="Warning !",
                                   message="Please, enter name to make a \
                                   research of record.")

    def erase(self):
        """ This method allows to erase a name is in the Annuaire. """
        erase_name = self.widgets_entry['name'].get()

        if erase_name:
            e_nb = 0
            for key, value in self.dict_record.items():
                if key == erase_name:
                    want_del = messagebox.askyesno(title='Warning',
                                                   message=('Do you want delete\
                                                    :' + str(key)))
                    if want_del:
                        self.dict_record.pop(key)
                    e_nb += 1
            if e_nb == 0:
                messagebox.showinfo(title="No result !",
                                    message="No name correspond to your \
                                    research.")
        else:
            messagebox.showwarning(title="Warning !",
                                   message="Please, enter name to delete \
                                   record.")


if __name__ == '__main__':
    app = Window()
    app.mainloop()
