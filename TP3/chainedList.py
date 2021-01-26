#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ChainedList():
    """
    Chained list Object

    Parameters
    ----------
    nodes : list
        list that we want to transfert in a chained list of Node object
    """
    def __init__(self):
        self.first_node = None

    def insert_node_after(self, data, new_node):
        """
        insert a new node after the node with the value == data

        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        node = self.first_node
        while node.data != data:
            node = node.link
        node_after_add = node.link
        node.link = new_node
        new_node.link = node_after_add

    def delete_node(self, data):
        """
        delete all node(s) value == data

        Parameters
        ----------
        data : searched data to delete
        """
        node = self.first_node
        while node.data != data:
            before = node
            node = node.link
        before.link = node.link.link
