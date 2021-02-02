#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author = Mégane Boujeant
"""

from tree_node import TreeNode
from tree_node_2 import Tree


def tree_course():
    node_0 = TreeNode("Leonardo")
    node_1 = TreeNode("L1")
    node_2 = TreeNode("L2")
    node_0.left_child = node_1
    node_0.right_child = node_2

    node_0.print_tree_node()

    print(node_0.is_leaf())
    print(node_1.is_leaf())

    arbre = Tree(node_0)

    arbre.transversal_deep()
    arbre.transversal_deep()


def tree_to_try_function():
    node_0 = TreeNode(1)
    node_1 = TreeNode(2)
    node_2 = TreeNode(3)
    node_0.left_child = node_1
    node_0.right_child = node_2
    node_3 = TreeNode(4)
    node_4 = TreeNode(5)
    node_1.left_child = node_3
    node_1.right_child = node_4
    node_5 = TreeNode(6)
    node_6 = TreeNode(7)
    node_2.left_child = node_5
    node_2.right_child = node_6

    arbre = Tree(node_0)

    return arbre

if __name__ == "__main__":
    # tree_course()
    tree = tree_to_try_function()
    tree.transversal_deep()
    tree.add_node("1bis", 1)    # try add node after first node of tree
    tree.add_node("2bis", 2)    # try add node after medium node
    tree.add_node("6bis", 6)    # try add node after last node of tree
    tree.add_node("Jamais", 45) # try add node after inexistant node
    tree.transversal_deep()
