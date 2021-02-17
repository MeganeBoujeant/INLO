# coding: utf-8
import json
from json import JSONEncoder

"""
Class User of the project

@author : Olivier CHABROL
"""
class MemDict:
    def __init__(self):
        self.dico = {}
        self.config = None
    
    def size(self):
        return len(self.dico)

    def load_model(self, config):
        self.config = config
        conf = None
        with open(self.config) as fh:
            conf = json.load(fh)
        print(conf)
        for key,value in conf.items():
            self.dico[key] = User.from_dict(value)
        print(self.dico)
    
    def save(self, config):
        self.config = config
        with open(self.config, "w") as fh:
            json.dump(self.dico, fh, cls=MyEncoder)
    
    def get(self, searchTerm):
        if searchTerm in self.dico:
            return self.dico[searchTerm]
        else:
            return None
    
    def delete(self, searchTerm):
        if searchTerm in self.dico:
            del self.dico[searchTerm]

    def insert(self, user):
        self.dico[user.last_name] = user

    def __str__(self):
        return str(self.dico)

class User:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.phone = None
        self.city = None
        self.age = 0

    @staticmethod
    def from_dict(dico):
        user = User()
        for elm in user.__dict__:
            user.__dict__[elm] = dico[elm]
        return user

    def to_dict(self):
        dico = {}
        dico["first_name"] = self.first_name
        dico["last_name"] = self.last_name
        dico["address"] = self.address
        dico["phone"] = self.phone
        dico["city"] = self.city
        dico["age"] = self.age
        return dico
    
    def get_key_field(self):
        return "last_name"
    
    def is_valid(self):
        list_error = []
        if self.last_name == None:
            list_error.append("veuillez définir votre nom")
        if self.first_name == None:
            list_error.append("veuillez définir votre prénom")
        if self.address == None:
            list_error.append("veuillez définir votre adresse")
        if self.phone == None:
            list_error.append("veuillez définir votre téléphone")
        if self.city == None:
            list_error.append("veuillez définir votre ville")
        if self.age == None and self.age is not int:
            list_error.append("veuillez définir votre age")
        if not(self.age and isinstance(self.age, int)):
            #if self.first_name and self.last_name and self.age > 0:
               # return True
            #else:
               # list_error.append("veuillez définir votre nom et prénom")
            list_error.append("votre age n'est pas correct")
        return list_error
        
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.first_name, self.last_name, self.address, self.phone, self.city, self.age)

class MyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)