#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author = Mégane Boujeant
"""

from tree_node import TreeNode
from tree_node_2 import Tree


if __name__ == "__main__":
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