#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""


class Tree:
    """ Tree of Node Object
    """
    def __init__(self, root_node):
        self.root_node = root_node

    def transversal_deep(self):
        """ Function to print the tree
        """
        print(self.root_node)

    def add_node(self, added_node, target_node):
        """ Function which allows to add a new node after a target node.

        Parameters
        ----------
        added_node :
            node data that we want to add
        target_node :
            node which is located before the new node that we want to add.
        """
        # if target_node is the first node
        if self.root_node.data == target_node:
            self.root_node.add_after(added_node)
            return

        # if target_node isn't the first node
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
        """ Function which allows to delete a target node of a tree.

        Parameters
        ----------
        target_node :
            node that we want to delete.
        """

        node_before = self.root_node

        r_child = self.root_node.visit_right()
        l_child = self.root_node.visit_left()

        if r_child:
            if r_child.data == target_node:
                self.root_node.del_node(node_before, "r")
                return
            elif l_child:
                if l_child.data == target_node:
                    self.root_node.del_node(node_before, "l")
                    return

        if not self.root_node.is_leaf():
            if self.root_node.right_child:
                tree_right = Tree(r_child)
                tree_right.delete_node(target_node)
            elif self.root_node.left_child:
                tree_left = Tree(l_child)
                tree_left.delete_node(target_node)
