#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Title: Example of course with french comments to understand

	Lors de l'execution des tests unitaires, si on veut voir le détail, on
	rajoute -v
"""

import sys
sys.path.append("..")
import mymath
import unittest


class TestAdd(unittest.TestCase):
	"""
	Test the add function from the mymath library
	"""

	def test_add_integers(self):
		"""
		Test that the addition of two integers returns the correct total
		"""
		result = mymath.add(1, 2)
		self.assertEqual(result, 3)
		# assertEqual est une méthode de la classe TestCase qui dit quel est
		# censé être le résultat du test effectué

	def test_add_floats(self):
		"""
		Test that the addition of two floats returns the correct result
		"""
		result = mymath.add(10.5, 2)
		self.assertEqual(result, 12.5)

	def test_add_strings(self):
		"""
		Test the addition of two strings returns the two string as one
		concatenated string
		"""
		result = mymath.add('abc', 'def')
		self.assertEqual(result, 'abcdef')


if __name__ == '__main__':
	unittest.main()
