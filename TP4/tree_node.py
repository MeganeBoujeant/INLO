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
            return "[ " + str(self.left_child) + " ; " + str(self.right_child) \
                   + " ] " + str(self.data)

    def visit_right(self):
        """ Function to return right child
        """
        return self.right_child

    def visit_left(self):
        """ Function to return left child
        """
        return self.left_child

    def add_after(self, value_new_node):
        """ Function to add a new node after a target node

        Parameters
        ----------
        value_new_node:
            value of the new node that we want to insert
        """
        if not self.right_child:
            self.right_child = TreeNode(value_new_node)
        elif not self.left_child:
            self.left_child = TreeNode(value_new_node)
        else:
            old_right_child = self.right_child
            self.right_child = TreeNode(value_new_node)
            self.right_child.right_child = old_right_child

    def del_node(self, parent_node, r_or_l):
        """ Function to delete a target node.

        Parameters
        ----------
        parent_node:
            parent node of the child that we want to delete
        r_or_l:
            right or left child that we want delete
        """
        if self.is_leaf():
            if r_or_l == "r":
                parent_node.right_child = None
            else:
                parent_node.left_child = None

        elif self.right_child and not self.left_child:
            if r_or_l == "r":
                parent_node.right_child = self.right_child
                self.right_child = None
            else:
                parent_node.left_child = self.right_child
                self.right_child = None

        elif not self.right_child and self.left_child:
            if r_or_l == "r":
                parent_node.right_child = self.left_child
                self.left_child = None
            else:
                parent_node.left_child = self.left_child
                self.left_child = None

        else:
        # 2 child -> replace by last right chils which don't have any child
            r_child = parent_node.right_child
            while r_child.right_child:
                parent = r_child
                r_child = r_child.right_child
            replace_node = r_child
            self.data = replace_node.data
            parent.right_child = None
