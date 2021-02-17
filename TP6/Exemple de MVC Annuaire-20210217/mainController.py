# coding: utf-8

from view import View
from model import User
from model import MemDict

"""
Class Controller of the project

@author : Olivier CHABROL
"""
class Controller:
    def __init__(self, modelManager):
        self.model_manager = modelManager
        self.view = View(self)
        self.model = User()
        self.modelConfig = None
    
    def set_model_config(self, config):
        self.model_manager.load_model(config)
    
    def save_model(self, fileName):
        self.model_manager.save(fileName)

    def main(self):
        print("[Controller][main]")
        lizt = []
        for elm in self.model.__dict__:
            lizt.append(elm.replace("_", " "))
        self.view.create_fields(lizt)
        self.view.main()
    
    def button_press_handle(self, buttonId):
        print("[Controller][button_press_handle] "+ buttonId)
        if buttonId == "Chercher":
            self.search()
        elif buttonId == "Effacer":
            self.delete()
        elif buttonId == "Inserer":
            self.insert()
        else:
            pass
    
    def search(self):
        mainField = self.model.get_key_field()
        search_key = self.view.get_text_from_field(mainField)
        print("[Controller][search] key : " + str(search_key))
        user = self.model_manager.get(search_key)
        if user != None:
            self.view.display_model(user.to_dict())

    def delete(self):
        search_key = self.view.get_text_from_field(self.model.get_key_field())
        print("[Controller][delete] key : " + str(search_key))
        self.model_manager.delete(search_key)

    def insert(self):
        print("[Controller][insert] key")
        fields = self.view.get_all_fields()
        verif = self.model.is_valid()
        if len(verif) == 0:
            print("[Controller][insert] key : " + str(fields))
            user = User()
            for elm in self.model.__dict__:
                setattr(user, elm, fields[elm])
            self.model_manager.insert(user)
            self.view.clear_fields()
            print(self.model_manager)
        else:
            self.view.erreur(verif)

    def save(self):
        print("[Controller][save]")
        if self.model_manager.size() > 0:
            self.view.save_file()
        
    
if __name__ == "__main__":
    directory = Controller(MemDict())
    directory.main()
