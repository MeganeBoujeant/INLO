#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author = Mégane Boujeant
"""

from node import Node


class ChainedList:
    """ Chained list Object

    Parameters
    ----------
    list_data : list
        list of data that we want to transfert in a chained list of Node object
    """
    def __init__(self, list_data: list):
        self.first_node = Node(list_data[0])
        node = self.first_node
        for pos in range(1, len(list_data)):
            node.link = Node(list_data[pos])
            node = node.link

    def __str__(self):
        node_list = []
        node = self.first_node
        while node.link:
            node_list.append(node.data)
            node = node.link
        node_list.append(node.data)
        return str(node_list)

    def insert_node_after(self, data: int, new_node_data: int):
        """ Insert a new node with data == new_node_data, after the node with
        the value == data

        Parameters
        ----------
        data : int
            searched data (whose we want insert new node after her)
        new_node_data : int
            new node to insert
        """
        node = self.first_node
        while node.data != data:
            node = node.link
        if node.data == data:   # Test of the exceptional case where no value
                                # in the chained list corresponds to data
            node_after_add = node.link
            new_node = Node(new_node_data)
            node.link = new_node
            new_node.link = node_after_add

    def delete_node(self, data: int):
        """ Delete all node(s) when value == data

        Parameters
        ----------
        data : int
            searched data to delete
        """
        while self.first_node.data == data:
            self.first_node = self.first_node.link

        node_before = self.first_node
        node = self.first_node.link

        while node.link:
            if node.data == data:
                node_before.link = node.link
                node = node_before.link
            else:
                node_before = node_before.link
                node = node.link

        if node.link is None:
            if node.data == data:
                node_before.link = None
