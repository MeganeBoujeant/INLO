#!/usr/bin/env python
# -*- coding: utf-8 -*-

from animal import Animal
from animal import Dog


if __name__ == "__main__":
	chien = Dog("Rex")
	chien.weight = 12
	chien.size = 40

	cat = Animal("Catus lupus familiaris")
	# cat.weight = 60
	cat.size = 4

	print(chien.__dict__)
	print(cat.__dict__)

	# cat.walk()

	cat1 = Animal("Catus lupus familiaris")
	cat1.size = -6
	print(cat1.__dict__)

	print(cat1 == cat)

	print(cat)
	print(cat1)
	print(chien)

	print(cat._species)
	print(cat1._species)

	chien.walk()
