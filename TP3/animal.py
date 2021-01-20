#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:

	def __init__(self, param_species):
		self.weight = 0
		self.size = 0
		self.species = param_species

	def walk(self):
		print("miaou miaou je marche")