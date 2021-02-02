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
        if self.root_node.data == target_node:
            self.root_node.add_after(added_node)
            return

        right_child = self.root_node.visit_right()
        left_child = self.root_node.visit_left()
        if right_child:
            if right_child.data == target_node:
                right_child.add_after(added_node)
                return
            elif left_child:
                if left_child.data == target_node:
                    left_child.add_after(added_node)
                    return

        if not self.root_node.is_leaf():
            if self.root_node.right_child:
                tree_right = Tree(right_child)
                tree_right.add_node(added_node, target_node)
            elif self.root_node.left_child:
                tree_left = Tree(left_child)
                tree_left.add_node(added_node, target_node)

    def delete_node(self, target_node):
        pass
