#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""


class TreeNode:
    """ Tree of Node Object
    """

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def print_tree_node(self):
        """ Function
        """
        if self.right_child:
            self.right_child.print_tree_node()
        print(self.data)
        if self.left_child:
            self.left_child.print_tree_node()

    def is_leaf(self):
        """ Function
        True : si feuille ou je suis est extremité (pas d'enfant)
        sinon false
        """
        return self.right_child is None and self.left_child is None

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        else:
            return "[ " + str(self.left_child) + " ; " + str(self.right_child) + " ] " + str(self.data)

    def create_tree(self):
        pass
