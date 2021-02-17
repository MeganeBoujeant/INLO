# coding: utf-8

import os
from tkinter import Button
from tkinter import Entry
from tkinter import filedialog 
from tkinter import Label
from tkinter import Menu
from tkinter import StringVar
from tkinter import Tk
from tkinter import messagebox
"""
Class View of the project

@author : Olivier CHABROL
"""
class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.buttons = ["Chercher", "Inserer", "Effacer"]
        self.modelListFields = []
        self.fileName = None

    

    def get_text_from_field(self, fieldName):
        return self.widgets_entry[fieldName.replace("_", " ")].get()

    def get_all_fields(self):
        fields = {}
        for key, value  in self.widgets_entry.items():
            fields[key.replace(" ", "_")] = value.get()
        return fields
    
    def clear_fields(self):
        for key, value  in self.widgets_entry.items():
            value.delete(0, 'end')

    def display_model(self, dico):
        print("[View] display_model " + str(dico))
        self.clear_fields()
        for key, value  in dico.items():
            self.widgets_entry[key.replace("_", " ")].insert(0, value)

        
    def main(self):
        print("[View] main")
        self.title("Annuaire")
        self.create_menu()
        self.mainloop()

    def create_menu(self):
        menubar = Menu(self)

        menuFile = Menu(menubar, tearoff=0)
        menuFile.add_command(label="Open", command=self.open_file, accelerator="Ctrl+o")
        menuFile.add_command(label="Save", command=self.save_file, accelerator="Ctrl+s")
        menuFile.add_separator()
        menuFile.add_command(label="Quit", command=self.quit, accelerator="Ctrl+q")
        menubar.add_cascade( label="File", menu=menuFile)
        self.bind_all("<Control-q>", self.quit)
        self.bind_all("<Control-o>", lambda e: self.open_file())
        self.bind_all("<Control-s>", lambda e: self.save_file())

        self.config(menu=menubar)

    def quit(self):
        self.controller.save()
        self.destroy()

    def save_file(self):
        if self.fileName == None:
            self.fileName = filedialog.asksaveasfilename(initialdir= os.getcwd(),title="Select File",filetypes=(("JSON files","*.json"),("Text Files", "*.txt"),("all files","*.*"))) 
        self.controller.save_model(self.fileName)


    def open_file(self):
        self.fileName = filedialog.askopenfilename(initialdir= os.getcwd(),title="Select File",filetypes=(("JSON files","*.json"),("Text Files", "*.txt"),("all files","*.*"))) 
        self.controller.set_model_config(self.fileName)

    
    def create_fields(self, modelListFields):
        self.modelListFields = modelListFields
        i, j  = 0, 0

        for idi in self.modelListFields:
            lab = Label(self, text=idi.capitalize())
            self.widgets_labs[idi] = lab
            lab.grid(row=i,column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            self.widgets_entry[idi] = entry
            entry.grid(row=i,column=1)

            i += 1

        for idi in self.buttons:
            buttonW = Button(self, text = idi, command=(lambda button=idi: self.controller.button_press_handle(button)))
            self.widgets_button[idi] = buttonW
            buttonW.grid(row=i+1,column=j)
            #self.widgets_button[idi].config(command = idi)

            j += 1

    def erreur(self, list_errors):
        messagebox.showwarning("Error", "Vous avez pas bien remplit les champs: \n" + '\n'.join(list_errors))

