#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""

from node import Node
from chained_list import ChainedList


def test_print_node():
    """ Function to test print node
    """
    node_1 = Node(1)
    node_2 = Node(5)
    node_1.link = node_2
    print("[test_print_node] " + str(node_1))
    print_recurs(node_1)


def print_recurs(param_node):
    print("[print_recurs] " + str(param_node.data))
    if param_node.link:
        next_node = param_node.link
        print_recurs(next_node)


def test_insert_value_chained_list(list_to_transform: list):
    """ Function to test the insertion of a node in a chained list.

    Parameters
    ----------
    list_to_transform: list
        list whose we want to transformed in a chained list
    """
    chained_list = ChainedList(list_to_transform)
    print("[Chained List initial ]" + str(chained_list))
    chained_list.insert_node_after(5, 12)
    print("[Chained List after new add ]" + str(chained_list))

    chained_list.insert_node_after(5, 6)
    print("[Chained List after new add ]" + str(chained_list))

    # Test with data value which don't exist
    chained_list.insert_node_after(845, 6)
    print("[Chained List after new add ]" + str(chained_list))

def test_delete_function(list_to_transform: list, data_to_delete: int):
    """ Function to test the deletion of all node(s) with data_to_delete value
     in a chained list.

    Parameters
    ----------
    list_to_transform: list
        list whose we want to transformed in a chained list
    data_to_delete: int
        value data that we want to delete in the chained list
    """
    chained_list = ChainedList(list_to_transform)
    chained_list.delete_node(data_to_delete)
    print("[Chained List after delete ]" + str(chained_list))


if __name__ == "__main__":
    # Just a test to see how the __str__ method of node work's
    test_print_node()

    # Tests functions of ChainedList class
    new_list = [1, 5]
    test_insert_value_chained_list(new_list)
    list_test_delete = [1, 5, 6, 5, 1, 12, 34]
    test_delete_function(list_test_delete, 1)
