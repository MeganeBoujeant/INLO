#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:

	def __init__(self, param_species):
		self.weight = 0
		self._size = 0
		self._species = param_species

	def _get_species(self):
		return self._species

	# Les 2 propriétés suivante ne servent à rien  sauf si on rajoute le if en set
	def _get_size(self):
		return self._size

	def _set_size(self, param_size):
		if (param_size < 0):
			self._size = 0
		else:
			self._size = param_size

	# Il existe 4 property : get, set, delete, helper
	species = property(_get_species)
	size = property(_get_size, _set_size)

	def walk(self):
		print("miaou miaou je marche")


	def __eq__(self, b):	# Il existe aussi des méthodes réservées pour plus petit ou plus grad que
		# return self.species == b.species and self.size == b.size and self.weight == b.weight
		# => méthode trop longue et fastidieuse
		return self.__dict__ == b.__dict__

	def __str__(self):
		return "Je suis un " +  self.species + " de taille " + str(self.size) + " cm."


class Dog(Animal):

	def __init__(self, param_name):
		super().__init__("Canis lupus familiaris")
		# Autre méthode pour faire le super() :
		# Animal.__init__(self, "Canis lupus familiaris") => cette méthode fonctionne plus ou moins selon la version de python utilisée
		self.name = param_name

	# Surchage de méthode : redéfinir walk en la spécifiant pour le chien
	def walk(self):
		print("wouaf wouaf je marche")
