#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""

from tree_node import TreeNode

class Tree:
    """ Tree of Node Object
    """

    def __init__(self, root_node):
        self.root_node = root_node

    def transversal_deep(self):
        """

        """
        print(self.root_node)

    def add_node(self, added_node, target_node):
        pass