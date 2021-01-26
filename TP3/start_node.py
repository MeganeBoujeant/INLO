#!/usr/bin/env python
# -*- coding: utf-8 -*-

from node import Node
from chainedList import *


def test_print_node():
    n1 = Node(1)
    n2 = Node(5)
    n1.link = n2
    print(n1)

def test_print_5_nodes():
    # With this values : 1, 5, 6, 12, 34
    n1 = Node(1)
    n2 = Node(5)
    n1.link = n2
    n3 = Node(6)
    n2.link = n3
    n4 = Node(12)
    n3.link = n4
    n5 = Node(34)
    n4.link = n5
    print(n1)


if __name__ == "__main__":
    # just a test to see how the __str__ method of node work's
    ## test_print_5_nodes()
    crea_list = test_print_node()
    chained_list = ChainedList.insert_node_after(crea_list, 5, 12)
    print(chained_list)
    chained_list = ChainedList.insert_node_after(crea_list, 5, 6)
    print(chained_list)
