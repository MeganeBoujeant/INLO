#!/usr/bin/env python
# -*- coding: utf-8 -*-

from animal import Animal


if __name__ == "__main__":
	chien = Animal("Canis lupus familiaris")
	chien.weight = 12
	chien.size = 40

	cat = Animal("Catus lupus familiaris")
	cat.weight = 60
	cat.size = 4

	print(chien.__dict__)
	print(cat.__dict__)

	cat.walk()