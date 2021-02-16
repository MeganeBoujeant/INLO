#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""

class Individu():

    def __init__(self, name, last_name, phone, adress, city):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.adress = adress
        self.city = city

    def __str__(self):
        return (self.name + self.last_name + self.phone + self.adress + self.city)
