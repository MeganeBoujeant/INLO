#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""

class Node:
    """ Node Object

    Parameters
    ----------
    param_data : int
        value of Node Object
    """

    def __init__(self, param_data: int):
        self.data = param_data
        self.link = None

    def __str__(self):
        node_list = []
        node = self
        while node.link:
            node_list.append(node.data)
            node = node.link
        node_list.append(node.data)
        return str(node_list)
