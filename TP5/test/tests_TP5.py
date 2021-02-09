#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant

    example of exception to understand :

        def divide(a, b):
            if b == 0:
                raise Exception("On ne divise pas par 0")
            return (a / b)

        if __name__ == "__main__":
            try:
                divide(5, 0)
            except Exception:
                print("You have an error")
"""

from linkedList import Node, LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    """ This class test functions of LinkedList class """

    def setUp(self):
        """ Tests initialization """
        self.linked_list = LinkedList(['a', 'b', 'c', 'd', 'e'])

    def test_new_linked_list_is_empty(self):
        """ Test 1 : test if a new linked list is empty """
        empty_list = LinkedList([])
        self.assertIsNone(empty_list, "The list is empty.")

    def test_add_pile_is_empty(self):
        """ Test 2 : test if a pile on which have just stacked an element is 
        not empty """
        self.linked_list.add_after('b', Node('f'))
        self.assertIsNotNone(self.linked_list, "Your list is empty")

    def test_add_delete_is_equal(self):
        """ Test 3 : a chained list that undergoes stacking followed by
        unstacking is unchanged"""
        list_changed = self.linked_list
        list_changed.add_after('d', Node('g'))
        list_changed.remove_node('g')
        self.assertEqual(list_changed, self.linked_list, "The final list is not the same that the start chained list")

    def test_added_top_is_top(self):
        """ Test 4 : the top of a pile on which we have just stacked an element 
        e is e """
        self.linked_list.add_first('m')
        self.assertEqual(self.linked_list.head, 'm', "fist is not first")

    def tearDown(self):
        """ Freeing up resources, closing any files open in setUp """


if __name__ == "__main__":
    unittest.main()
