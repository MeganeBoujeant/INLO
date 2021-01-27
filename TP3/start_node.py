#!/usr/bin/env python
# -*- coding: utf-8 -*-

from node import Node
from chainedList import ChainedList


def test_print_node():
    n1 = Node(1)
    n2 = Node(5)
    n1.link = n2
    return n1


def test_class_chained_list(list_to_transform: list):
    chained_list = ChainedList(list_to_transform)
    print(chained_list)
    chained_list.insert_node_after(5, 12)
    print(chained_list)

    chained_list.insert_node_after(5, 6)
    print(chained_list)


def test_delete_function(list_to_transform: list, data_to_delete: int):
    chained_list = ChainedList(list_to_transform)
    chained_list.delete_node(data_to_delete)
    print(chained_list)


if __name__ == "__main__":
    # just a test to see how the __str__ method of node work's
    test_print_node()
    new_list = [1, 5]
    test_class_chained_list(new_list)
    list_test_delete = [1, 5, 6, 5, 1, 12, 34]
    test_delete_function(list_test_delete, 1)
